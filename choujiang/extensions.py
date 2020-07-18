from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
"""
第三方扩展插件
"""
db = SQLAlchemy(session_options={'expire_on_commit': False})
migrate = Migrate()