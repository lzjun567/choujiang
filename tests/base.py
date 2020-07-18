import datetime
import json
import unittest
import urllib.parse

from faker import Faker
from flask import url_for

from choujiang import create_app
from choujiang import db

fake = Faker("zh_CN")


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app('testing')
        self.context = app.test_request_context()
        self.context.push()
        self.client = app.test_client()
        self.fake = Faker("zh_CN")
        self.runner = app.test_cli_runner()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.context.pop()

