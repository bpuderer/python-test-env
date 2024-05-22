from http import HTTPStatus
import logging
import xml.etree.ElementTree as ET

import requests

from framework.config import settings
from tests.base_test import BaseTestCase
from utils.schemavalidation.validate import validate_a


log = logging.getLogger(__name__)

class RestXmlExample(BaseTestCase):

    @staticmethod
    def send_xml(filename):
        with open(filename) as f:
            data = f.read()
        headers = {"Content-Type": "txt/xml"}
        return requests.post(settings["echoxml_url"], data=data, headers=headers,
                             timeout=float(settings["http_timeout"]))

    def send_xml_validate(self, filename):
        r = self.send_xml(filename)
        log.debug("Received: " + r.text)
        self.assertEqual(r.status_code, HTTPStatus.OK)
        validate_a(r.text)
        return ET.fromstring(r.text)


    def test_xml(self):
        """xml test using flask_http_sim.py in python-test"""
        expected = {"b val 1", "b val 2"}
        root = self.send_xml_validate("resources/requests/echoxml/request1.xml")
        b_elements = root.iterfind('b')
        b_vals = {b.text for b in b_elements}
        self.assertEqual(b_vals, expected)


    def test_xml_malformed(self):
        """test to demo schema check failing"""
        self.send_xml_validate("resources/requests/echoxml/malformed.xml")
