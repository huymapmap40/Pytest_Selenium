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
    def SetWait(wait):
        BaseConfig.__wait = wait

    @staticmethod
    def GetWait():
        return BaseConfig.__wait

    @staticmethod
    def SetDriver(driver):
        BaseConfig.__driver = driver

    @staticmethod
    def GetDriver():
        return BaseConfig.__driver

    @property
    def BrowserName(self):
        return self.__browserName

    @BrowserName.setter
    def BrowserName(self, value):
        self.__browserName = value

    @property
    def RemoteAddress(self):
        return self.__remoteAddress

    @RemoteAddress.setter
    def RemoteAddress(self, value):
        self.__remoteAddress = value

    @staticmethod
    def GetInstance():
        if BaseConfig.__instance == None:
            BaseConfig.__instance = BaseConfig()
        return BaseConfig.__instance

    def ShutDown(self):
        BaseConfig.__driver.quit()

    def SetUp(self):
        config_dir = path.dirname(path.dirname(__file__))
        with open(path.join(config_dir, 'config_env_test')) as f:
            data_setup = json.load(f)
            self.RemoteAddress = data_setup['remoteAddress']
            self.BrowserName = data_setup['browserName']
            driver = webdriver.Remote(command_executor=self.RemoteAddress, desired_capabilities={'browserName': self.BrowserName})
            wait = WebDriverWait(driver, Constant.DRIVER_TIMEOUT)
            BaseConfig.SetDriver(driver)
            BaseConfig.SetWait(wait)
