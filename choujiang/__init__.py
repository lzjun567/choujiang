import datetime
import logging
import os
import traceback
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.contrib.profiler import ProfilerMiddleware

from choujiang import services
from choujiang.blueprints.web import web_bp
from choujiang.extensions import  db, migrate
from choujiang.settings import config
from choujiang.utils import CustomJSONEncoder
from .cli import register_commands

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def create_app(config_name=None):
    if not config_name:
        config_name = os.getenv('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.json_encoder = CustomJSONEncoder

    register_logging(app)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errors(app)
    register_hook(app)
    # TODO 后面前端CSS资源优化完之后考虑引进
    app.jinja_env.globals['url_for_other_page'] = url_for_other_page
    global celery
    return app


def url_for_other_page(page):
    args = request.view_args.copy()
    args.update(request.args)
    args['page'] = page
    return url_for(request.endpoint, **args)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(web_bp, url_prefix="")

def register_logging(app):
    class RequestFormatter(logging.Formatter):

        def format(self, record):
            record.url = request.url
            record.remote_addr = request.remote_addr
            return super(RequestFormatter, self).format(record)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if not os.path.exists("logs"):
        os.mkdir("logs")

    file_handler = RotatingFileHandler(os.path.join(basedir, 'logs/choujiang.log'),
                                       maxBytes=10 * 1024 * 1024, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)


def register_errors(app):
    @app.errorhandler(400)
    def bad_404_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(403)
    def bad_403_request(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        app.logger.error('%s %s %s 500 INTERNAL SERVER ERROR \nREQUEST DATA:\n%s', request.remote_addr,
                         request.method, request.full_path, request.data)
        app.logger.error(e, exc_info=True)
        return render_template('errors/500.html'), 500


def register_hook(app):
    from flask_sqlalchemy import get_debug_queries

    if app.config.get('PROFILE'):
        """
        性能监测
        """
        app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

        @app.after_request
        def slow_query(response):
            for query in get_debug_queries():
                if query.duration >= app.config['DATABASE_QUERY_TIMEOUT']:
                    app.logger.warning("SLOW QUERY: %s\nParameters: %s\nDuration: %fs\nContext: %s\n" % (
                        query.statement, query.parameters, query.duration, query.context))
            return response

