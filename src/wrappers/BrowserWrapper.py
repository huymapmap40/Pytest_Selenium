from src.utilities.Constant import Constant
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, JavascriptException
from src.config.setup.BaseConfig import BaseConfig
from selenium import webdriver


class BrowserWrapper:
    # webdriver.Firefox().find_element(By.XPATH,...)
    __currentBrowserDriver = None

    def __init__(self):
        BrowserWrapper.driver_instance()

    # Get webdriver instance
    @staticmethod
    def driver_instance():
        try:
            if BrowserWrapper.__currentBrowserDriver is None:
                base_config_object = BaseConfig()
                base_config_object.set_up()
                BrowserWrapper.__currentBrowserDriver = base_config_object.get_driver()
        except:
            raise WebDriverException("Could not setup webdriver")
        return BrowserWrapper.__currentBrowserDriver

    def set_page_load_timeout(self, timeout_in_second):
        BrowserWrapper.driver_instance().set_page_load_timeout(timeout_in_second)

    def set_element_timeout(self, timeout_in_second):
        BrowserWrapper.driver_instance().implicitly_wait(timeout_in_second)

    def maximize_window_browser(self):
        BrowserWrapper.driver_instance().maximize_window()

    def go_to_url(self, url):
        current_driver = BrowserWrapper.driver_instance()
        current_driver.get(url)
        WebDriverWait(current_driver, Constant.DRIVER_TIMEOUT).until(
            lambda x: x.execute_script("return document.readyState") == "complete")
        self.set_page_load_timeout(Constant.PAGE_LOAD_TIMEOUT)
        self.set_element_timeout(Constant.ELEMENT_TIMEOUT)

    @staticmethod
    def execute_javascript(script_string, *args):
        try:
            return BrowserWrapper.driver_instance().execute_script(script_string, args)
        except:
            raise JavascriptException("Could not execute the script '{}'".format(script_string))

    @staticmethod
    def refresh_page():
        BrowserWrapper.driver_instance().refresh()

    def quit(self):
        BrowserWrapper.driver_instance().quit()
