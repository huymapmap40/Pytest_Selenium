import pytest
from src.wrappers.browser_wrapper import BrowserWrapper


@pytest.mark.usefixtures("setup_driver")
class TestBase:

    # @staticmethod
    def setup_test(self, url):
        print("Setup the test")
        global browserObj
        browserObj = BrowserWrapper(self.driver)
        browserObj.maximize_window_browser()
        browserObj.go_to_url(url)

    # @staticmethod
    def cleanup_test(self):
        print("Setup the test")
        browserObj.quit()
