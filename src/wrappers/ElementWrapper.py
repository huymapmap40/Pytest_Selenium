from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from src.utilities.Constant import Constant
from src.wrappers.BrowserWrapper import BrowserWrapper
from selenium import webdriver


class ElementWrapper:

    def __init__(self, locator, value):
        self.__locator = locator
        self.__value = value
        self.__wait = WebDriverWait(BrowserWrapper.GetDriverInstance(), Constant.ELEMENT_TIMEOUT)

    # Method to get element by locator and it's value
    def __Map(self):
        try:
            return BrowserWrapper.GetDriverInstance().find_element(self.__locator, self.__value)
        except:
            raise NoSuchElementException("Not found element by {} with value '{}'".format(self.__locator, self.__value))

