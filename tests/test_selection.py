"""Demo selecting tests with nose2 attrib plugin.


-A slow
-A \!slow  **same as**  -A '!slow'

-A life=42

NOTE: run_tests.py uses a single -A argument, not multiple as with nose2
-A slow,tags=tag2  **with comma = AND**
-A slow tags=tag2  **no comma = OR**
-A tags=tag1,tags=tag3
-A tags=tag1 tags=tag3

https://nose2.readthedocs.io/en/latest/plugins/attrib.html?highlight=attribute
"""

from tests.base_test import BaseTestCase


class TestCaseSelection(BaseTestCase):
    """Demo basics of using test environment"""

    def test_timeouts(self):
        """Demo test selection - test_timeouts"""
        pass
    test_timeouts.slow = True


    def test_something1(self):
        """Demo test selection - test_something1"""
        pass
    test_something1.life = 41

    def test_something2(self):
        """Demo test selection - test_something2"""
        pass
    test_something2.life = 42


    def test_no_attr_tags(self):
        """Demo test selection - test_no_attr_tags"""
        pass


    def test_feature_scenario1(self):
        """Demo test selection - test_feature_scenario1"""
        pass
    test_feature_scenario1.tags = ['tag1']

    def test_feature_scenario2(self):
        """Demo test selection - test_feature_scenario2"""
        pass
    test_feature_scenario2.slow = True
    test_feature_scenario2.tags = ['tag2']

    def test_feature_scenario3(self):
        """Demo test selection - test_feature_scenario3"""
        pass
    test_feature_scenario3.tags = ['tag1', 'tag2']

    def test_feature_scenario4(self):
        """Demo test selection - test_feature_scenario4"""
        pass
    test_feature_scenario4.tags = ['tag1', 'tag3']
