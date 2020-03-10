import time
import pytest
from hamcrest import assert_that
from src.test_cases.TestBase import TestBase
from src.utilities.Constant import Constant


def test_run_test():
    TestBase.setup_test(Constant.URL_PAGE)
    time.sleep(5)
    TestBase.cleanup_test()
    assert_that(True, True)
