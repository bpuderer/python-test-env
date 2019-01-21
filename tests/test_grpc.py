"""Demo using test environment for grpc testing"""

import logging

from google.protobuf import json_format

from framework.config import settings
from framework.testbase import BaseTestCase
from utils.channel_factory import get_channel
from utils.builders.grpc_builders import build_number_from_file, build_number_from_dict
from services.doubler.doubler_pb2_grpc import DoublerStub
from services.doubler.doubler_pb2 import Number

log = logging.getLogger(__name__)


class ExampleGrpcTestCase(BaseTestCase):
    """Tests use server from grpc-demo/doubler"""

    @classmethod
    def setUpClass(cls):
        """test class setup"""
        cls._channel = get_channel(settings["doubler_grpc_host"], settings["doubler_grpc_port"])
        cls._stub = DoublerStub(cls._channel)

    @classmethod
    def tearDownClass(cls):
        """tearDownClass runs after tests"""
        cls._channel.close()

    def test_grpc_call1(self):
        """grpc call test1"""
        request = build_number_from_file('resources/requests/doubler/request1.json')
        response = self._stub.Double(request)
        log.debug(f'response: {json_format.MessageToJson(response)}')
        self.assertEqual(response.value, 10.0)

    def test_grpc_call2(self):
        """grpc call test2"""
        request = build_number_from_dict({'value': -4.0})
        response = self._stub.Double(request)
        self.assertEqual(response.value, -8.0)

    def test_grpc_call3(self):
        """grpc call test3"""
        request = Number(value=3.0)
        response = self._stub.Double(request)
        self.assertEqual(response.value, 6.0)
