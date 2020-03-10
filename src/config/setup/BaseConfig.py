import json
from os import path
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utilities.Constant import Constant

class BaseConfig:
    __instance = None
    __driver = None
    __browserName = None
    __wait = None
    __remoteAddress = None

    @staticmethod
    def set_wait(wait):
        BaseConfig.__wait = wait

    @staticmethod
    def get_wait():
        return BaseConfig.__wait

    @staticmethod
    def set_driver(driver):
        BaseConfig.__driver = driver

    @staticmethod
    def get_driver():
        return BaseConfig.__driver

    @property
    def browser_name(self):
        return self.__browserName

    @browser_name.setter
    def browser_name(self, value):
        self.__browserName = value

    @property
    def remote_address(self):
        return self.__remoteAddress

    @remote_address.setter
    def remote_address(self, value):
        self.__remoteAddress = value

    @staticmethod
    def get_instance():
        if BaseConfig.__instance == None:
            BaseConfig.__instance = BaseConfig()
        return BaseConfig.__instance

    def shut_down(self):
        BaseConfig.__driver.quit()

    def set_up(self):
        config_dir = path.dirname(path.dirname(__file__))
        with open(path.join(config_dir, 'config_env_test')) as f:
            data_setup = json.load(f)
            self.remote_address = data_setup['remoteAddress']
            self.browser_name = data_setup['browserName']
            driver = webdriver.Remote(command_executor=self.remote_address, desired_capabilities={'browserName': self.browser_name})
            wait = WebDriverWait(driver, Constant.DRIVER_TIMEOUT)
            BaseConfig.set_driver(driver)
            BaseConfig.set_wait(wait)
