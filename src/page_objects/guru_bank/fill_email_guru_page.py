from __future__ import annotations
from selenium.webdriver.common.by import By
from src.wrappers.element_wrapper import ElementWrapper


class FillEmailGuruPage:
    __instance: FillEmailGuruPage = None

    # Locators
    _txt_email_address = ElementWrapper((By.XPATH, "//input[@name='emailid']"))
    _btn_submit = ElementWrapper((By.XPATH, "//input[@name='btnLogin']"))
    _txt_user_name = ElementWrapper((By.XPATH, "//td[@class='accpage'][contains(text(),'User ID')]/following-sibling::td"))
    _txt_passwd = ElementWrapper((By.XPATH, "//td[@class='accpage'][contains(text(),'Password')]/following-sibling::td"))

    @staticmethod
    def get_instance():
        if FillEmailGuruPage.__instance is None:
            FillEmailGuruPage.__instance = FillEmailGuruPage()
        return FillEmailGuruPage.__instance

    def fill_email_address(self, email_value: str) -> None:
        self._txt_email_address.type(email_value)

    def click_submit(self) -> None:
        self._btn_submit.click()

    def fill_email_and_submit(self, email_value: str) -> None:
        self.fill_email_address(email_value)
        self.click_submit()

    def get_user_name(self) -> str:
        return self._txt_user_name.get_text()

    def get_password(self) -> str:
        return self._txt_passwd.get_text()
