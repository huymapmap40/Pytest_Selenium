import allure
import pytest
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to
from src.test_cases.test_base import TestBase
from src.test_data.general.page_urls import PageUrls
from src.wrappers.browser_wrapper import BrowserWrapper
from src.page_objects.guru_telecom.home_page_telecom import HomePageTelecom


@allure.severity(allure.severity_level.NORMAL)
def test_run_test():

    TestBase.setup_test(PageUrls.TELECOM_PAGE)
    home_page_telecom_obj = HomePageTelecom.get_instance()
    is_homepage_title = home_page_telecom_obj.is_homepage_title_displayed()
    assert_that(is_homepage_title, equal_to(True))
    allure.attach(BrowserWrapper().get_screenshot_png(), name= "Test allure", attachment_type=AttachmentType.PNG)
    TestBase.cleanup_test()
