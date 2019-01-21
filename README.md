# python-test-env

Simple test environment utilizing [nose2](https://github.com/nose-devs/nose2) and [unittest](https://docs.python.org/3/library/unittest.html).

Tests are added to *tests* and extend *framework.testbase.BaseTestCase* or unittest.TestCase.

Test settings are defined in *framework/test_settings.cfg* and are accessed using the *settings* dictionary in *framework.config*. The case-sensitive section name is used to specify the target environment and passed as an argument to *run_tests.py*. See [configparser](https://docs.python.org/3/library/configparser.html) for details.

Logs are written to the *log* directory and is configured using *framework/logging.cfg*.  See [logging](https://docs.python.org/3/library/logging.html) for details.

JUnit XML reports are written to the *reports* directory.

Test utilities can be added to *utils* and misc things needed by the tests can be added to *resources*. Modules needed by clients can be added to *services*. Screenshots taken by Selenium can be written to *screenshots*.

*run_tests.py* acts as the test runner by wrapping nose2, cleaning up the previous run's output files, and setting the **PY_TEST_ENV** environment variable which corresponds to the section name in *framework/test_settings.cfg* used by *framework.config*.


    $ python run_tests.py
    $ python run_tests.py -te env1 --xml
    $ python run_tests.py tests.test_example tests.test_example2 -te env1
    $ python run_tests.py --help
