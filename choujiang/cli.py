"""
命令行工具
"""
import click
from .extensions import db
from .models import Award
import random


def register_commands(app):
    @app.cli.command("init_data")
    def init_data():
        """
        初始化数据
        """
        click.echo("starting")
        for i in range(500):
            number = "".join([str(random.randint(0, 9)) for i in range(7)])
            award = Award(number=number, valid=False)
            if i % 100 == 0:
                award.valid = True
            db.session.add(award)
            db.session.commit()

        click.echo("finished")
