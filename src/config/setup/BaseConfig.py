import json
import collections
from os import path
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from src.utilities.constant import Constant


class BaseConfig:

    __instance = None

    @staticmethod
    def get_instance():
        if BaseConfig.__instance is None:
            BaseConfig.__instance = BaseConfig()
        return BaseConfig.__instance

    def shut_down(self):
        BaseConfig.__driver.quit()

    def init_driver(self, **kwargs):
        config_dir = path.dirname(path.dirname(__file__))
        with open(path.join(config_dir, 'config_env_test.json')) as f:
            data_setup = json.load(f)
            initial_driver = None
            if data_setup['configInfo']['enableRemoteWebDriver']:
                remote_address = data_setup['remoteWebDriver']['remoteAddress']
                # desired_capabilities = data_setup['remoteWebDriver']['desiredCapabilities'][1] # Chrome
                desired_capabilities = {"browserName": kwargs["browser_name"], "platform": "ANY"}
                initial_driver = webdriver.Remote(command_executor=remote_address,
                                        desired_capabilities=desired_capabilities)
            else:
                browser_name = data_setup['localWebDriver']['browserName']
                if browser_name == Constant.CHROME_BROWSER:
                    initial_driver = webdriver.Chrome(executable_path=path.abspath("drivers/chromedriver.exe"))
                elif browser_name == Constant.FIREFOX_BROWSER:
                    initial_driver = webdriver.Firefox(executable_path=path.abspath("drivers/geckodriver.exe"))
                else:
                    raise KeyError("Browser name not found!")
            initial_wait = WebDriverWait(initial_driver, Constant.DRIVER_TIMEOUT)
            web_init = collections.namedtuple('WebInit', ['Driver', 'Wait'])
            return web_init(initial_driver, initial_wait)
                    