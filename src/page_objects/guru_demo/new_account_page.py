from selenium.webdriver.common.by import By
from src.wrappers.element_wrapper import ElementWrapper
from typing import TypeVar

class NewAccountPage:
    __instance = None

    # Locators
    _txt_customer_id = ElementWrapper((By.XPATH, "//input[@name='cusid']"))
    _ddl_account_type = ElementWrapper((By.XPATH, "//select[@name='selaccount']"))
    _txt_deposit_initial = ElementWrapper((By.XPATH, "//input[@name='inideposit']"))
    _btn_submit = ElementWrapper((By.XPATH, "//input[@value='submit']"))
    _lbl_success_creation = ElementWrapper((By.XPATH, "//table[@id='account']//p[@class='heading3']"))

    # Dynamic controls
    def _opt_account_type(self, account_type: str) -> ElementWrapper:
        return ElementWrapper((By.XPATH, "//select[@name='selaccount']/option[@value='{}']".format(account_type)))

    def _account_info(self, info_type: str) -> ElementWrapper:
        return ElementWrapper((By.XPATH, "//td[text()='{}']/following-sibling::td".format(info_type)))

    @staticmethod
    def get_instance():
        if NewAccountPage.__instance is None:
            NewAccountPage.__instance = NewAccountPage()
        return NewAccountPage.__instance
