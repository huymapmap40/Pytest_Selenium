from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from src.utilities.constant import Constant
from src.wrappers.browser_wrapper import BrowserWrapper
from typing import Tuple
from selenium import webdriver


class ElementWrapper:

    # locator argument input is equivalent with tuple (By.xx , value_of_by)
    def __init__(self, locator: Tuple[By, str]):
        self.__locator = locator
        self.__wait = WebDriverWait(BrowserWrapper.driver_instance(), Constant.ELEMENT_TIMEOUT)

    # Method to get element by locator and it's value
    def __map(self):
        try:
            return BrowserWrapper.driver_instance().find_element(self.__locator[0], self.__locator[1])
        except NoSuchElementException as E:
            print(E)
            print("Not found element by {} with value '{}'".format(self.__locator[0], self.__locator[1]))

    def wait_clickable(self):
        self.__wait.until(EC.element_to_be_clickable(self.__locator))

    def wait_for_presence_of(self):
        self.__wait.until(EC.presence_of_element_located(self.__locator))

    def wait_for_visibility_of(self):
        self.__wait.until(EC.visibility_of_element_located(self.__locator))

    def click(self):
        self.wait_clickable()
        self.__map().click()

    def is_element_displayed(self):
        self.wait_for_visibility_of()
        try:
            return self.__map().is_displayed()
        except ElementNotVisibleException as E:
            print(E)

    def get_element_count(self):
        self.__map().find_elements(self.__locator[0], self.__locator[1]).count()

    def type(self, text):
        self.wait_for_visibility_of()
        try:
            return self.__map().send_keys(text)
        except ElementNotVisibleException as E:
            print(E)

    def get_text(self):
        self.wait_for_visibility_of()
        try:
            return self.__map().text
        except ElementNotVisibleException as E:
            print(E)

    def move_mouse_and_click(self):
        action = ActionChains(BrowserWrapper.driver_instance())
        try:
            action.move_to_element(self.__map()).click().perform()
        except MoveTargetOutOfBoundsException as E:
            print(E)


    # webdriver.Firefox.find_element()