from http import HTTPStatus
import json

import requests

from framework.config import settings
from tests.base_test import BaseTestCase


class RestJsonExample(BaseTestCase):

    def setUp(self):
        """test setup"""
        self.remove_books()

    def tearDown(self):
        """test cleanup"""
        self.remove_books()

    @staticmethod
    def create_book(filename):
        with open(filename) as f:
            book = json.load(f)
        return requests.post(settings["books_url"], json=book, timeout=float(settings["http_timeout"]))

    @staticmethod
    def remove_books():
        requests.delete(settings["books_url"], timeout=float(settings["http_timeout"]))


    def test_book_creation(self):
        """verify book creation using flask_http_sim.py in python-test"""
        r = self.create_book("resources/requests/books/request1.json")
        self.assertEqual(r.status_code, HTTPStatus.CREATED)
