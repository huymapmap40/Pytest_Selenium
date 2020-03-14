from selenium.webdriver.common.by import By
from src.wrappers.element_wrapper import ElementWrapper
from .manager_page import ManagerPage


class LoginPage:
    __instance = None

    # Init login page element
    _input_user_id = ElementWrapper((By.XPATH, "//input[@name='uid']"))
    _input_pwd = ElementWrapper((By.XPATH, "//input[@name='password']"))
    _btn_login = ElementWrapper((By.XPATH, "//input[@name='btnLogin']"))
    _btn_reset = ElementWrapper((By.XPATH, "//input[@name='btnReset']"))

    @staticmethod
    def get_instance():
        if LoginPage.__instance is None:
            LoginPage.__instance = LoginPage()
        return LoginPage.__instance

    def login_to_manager_page(self, user_name, pwd):
        self._input_user_id.type(user_name)
        self._input_pwd.type(pwd)
        self._btn_login.click()
        return ManagerPage.get_instance()

