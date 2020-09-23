import pytest
import warnings
import urllib3
from selenium import webdriver
from src.config.setup.BaseConfig import BaseConfig

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None, help="Define browser to run")

@pytest.fixture(scope="class")
def setup_driver(request):
    global driver
    browserName = request.config.getoption("--browser")
    if browserName is not None:
        BaseConfig.get_instance().set_up(browser_name=browserName)
        driver = BaseConfig.get_driver()
    request.cls.driver = driver
    yield
    driver.quit()
