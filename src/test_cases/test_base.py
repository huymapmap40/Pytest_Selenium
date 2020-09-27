import pytest
from src.wrappers.browser_wrapper import BrowserWrapper


@pytest.mark.usefixtures("setup_driver")
class TestBase:

    # @staticmethod
    def setup_test(self, url):
        print("Setup the test")
        # global browser_handle
        browser_handle = BrowserWrapper.instance()
        browser_handle.maximize_window_browser()
        browser_handle.go_to_url(url)

    # @staticmethod
    # def cleanup_test(self):
    #     print("Setup the test")
    #     browser_handle.quit()
