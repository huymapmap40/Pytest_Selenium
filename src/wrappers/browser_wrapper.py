from src.utilities.constant import Constant
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, JavascriptException
from src.config.setup.BaseConfig import BaseConfig
from selenium import webdriver


class BrowserWrapper:
    # webdriver.Firefox().get_screenshot_as_png()
    __currentBrowserDriver = None

    def __init__(self, driver):
        self.driver = driver
        BrowserWrapper.__currentBrowserDriver = self.driver

    @staticmethod
    def instance():
        return BrowserWrapper.__currentBrowserDriver

    # Get web driver instance
    @staticmethod
    def driver_instance():
        try:
            if BrowserWrapper.__currentBrowserDriver is None:
                # base_config_object = BaseConfig()
                # base_config_object.set_up()
                # BrowserWrapper.__currentBrowserDriver = base_config_object.get_driver()
                BrowserWrapper.__currentBrowserDriver = BrowserWrapper()
        except:
            raise WebDriverException("Could not setup web driver")
        return BrowserWrapper.__currentBrowserDriver

    def set_page_load_timeout(self, timeout_in_second):
        BrowserWrapper.instance().set_page_load_timeout(timeout_in_second)

    def set_element_timeout(self, timeout_in_second):
        BrowserWrapper.instance().implicitly_wait(timeout_in_second)

    def maximize_window_browser(self):
        BrowserWrapper.instance().maximize_window()

    def go_to_url(self, url):
        current_driver = BrowserWrapper.instance()
        current_driver.get(url)
        WebDriverWait(current_driver, Constant.DRIVER_TIMEOUT).until(
            lambda x: x.execute_script("return document.readyState") == "complete")
        self.set_page_load_timeout(Constant.PAGE_LOAD_TIMEOUT)
        self.set_element_timeout(Constant.ELEMENT_TIMEOUT)

    def get_screenshot_png(self):
        return BrowserWrapper.instance().get_screenshot_as_png()

    @staticmethod
    def is_alert_displayed():
        wait = WebDriverWait(BrowserWrapper.instance(), Constant.MIDDLE_TIMEOUT)
        return False if wait.until(EC.alert_is_present()) is None else True

    @staticmethod
    def accept_alert():
        BrowserWrapper.instance().switch_to.alert.accept()

    @staticmethod
    def cancel_alert():
        BrowserWrapper.instance().switch_to.alert.dismiss()

    @staticmethod
    def execute_javascript(script_string, *args):
        try:
            return BrowserWrapper.instance().execute_script(script_string, args)
        except:
            raise JavascriptException("Could not execute the script '{}'".format(script_string))

    @staticmethod
    def refresh_page():
        BrowserWrapper.instance().refresh()

    def quit(self):
        BrowserWrapper.instance().quit()
