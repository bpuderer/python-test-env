"""Base test case"""

import unittest


class BaseTestCase(unittest.TestCase):
    """Base test case"""

    def assertEndsInR(self, seq):
        """Assert last element in sequence is r or R"""
        if seq[-1].lower() != 'r':
            raise AssertionError(f"'{seq}' does not end in 'r' or 'R'")

    def assertSecondsApart(self, d1, d2, sec=0.5):
        """Assert two dates, datetimes or timedeltas are <= n seconds apart"""
        sec_apart = abs((d1-d2).total_seconds())
        if sec_apart > abs(sec):
            raise AssertionError(f'{d1} and {d2} are {sec_apart}s apart which exceeds {abs(sec)}s')
