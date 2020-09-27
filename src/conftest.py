import pytest
import warnings
import urllib3
from selenium import webdriver
from src.config.setup.BaseConfig import BaseConfig
from src.wrappers.browser_wrapper import BrowserWrapper


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None, help="Define browser to run")

@pytest.fixture(scope="class")
def setup_driver(request):
    browserName = request.config.getoption("--browser")
    if browserName is not None:
        config = BaseConfig.get_instance().init_driver(browser_name=browserName)
    else:
        config = BaseConfig.get_instance().init_driver()
    BrowserWrapper.inject_driver(config.Driver)
    request.cls.driver = config.Driver
    yield
    config.Driver.quit()
