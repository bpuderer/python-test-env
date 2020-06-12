"""Demo basics of using test environment"""

import logging

import framework.config
from tests.base_test import BaseTestCase

log = logging.getLogger(__name__)


class ExampleTestCase2(BaseTestCase):
    """Demo basics of using test environment"""

    def test_foo(self):
        """Another test demo in diff class for a better report"""
        log.info("executing ExampleTestCase2.test_foo")
