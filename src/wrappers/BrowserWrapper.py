from src.utilities.Constant import Constant
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from src.config.setup.BaseConfig import BaseConfig
from selenium import webdriver

class BrowserWrapper:
    # webdriver.Firefox().find_element(By.XPATH,...)
    __currentBrowserDriver = None

    def __init__(self):
        BrowserWrapper.GetDriverInstance()

    # Get webdriver instance
    @staticmethod
    def GetDriverInstance():
        try:
            if BrowserWrapper.__currentBrowserDriver is None:
                base_config_object = BaseConfig()
                base_config_object.SetUp()
                BrowserWrapper.__currentBrowserDriver = base_config_object.GetDriver()
        except:
            raise WebDriverException("Could not setup webdriver")
        return BrowserWrapper.__currentBrowserDriver

    def SetPageLoadTimeOut(self, timeOutInSecond):
        BrowserWrapper.GetDriverInstance().set_page_load_timeout(timeOutInSecond)

    def SetElementTimeOut(self, timeOutInSecond):
        BrowserWrapper.GetDriverInstance().implicitly_wait(timeOutInSecond)

    def MaximizeWindow(self):
        BrowserWrapper.GetDriverInstance().maximize_window()

    def GoToUrl(self, url):
        currentDriver = BrowserWrapper.GetDriverInstance()
        currentDriver.get(url)
        WebDriverWait(currentDriver, Constant.DRIVER_TIMEOUT).until(lambda x: x.execute_script("return document.readyState") == "complete")
        self.SetPageLoadTimeOut(Constant.PAGE_LOAD_TIMEOUT)
        self.SetElementTimeOut(Constant.ELEMENT_TIMEOUT)

    @staticmethod
    def ExecuteScript(scriptString, *args):
        return BrowserWrapper.GetDriverInstance().execute_script(scriptString, args)

    @staticmethod
    def RefreshPage():
        BrowserWrapper.GetDriverInstance().refresh()

    def Quit(self):
        BrowserWrapper.GetDriverInstance().quit()
