from __future__ import annotations
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

    def add_new_account(self, customer_id: str, account_type: str, deposit_initial: int) -> None:
        self._txt_customer_id.type(customer_id)
        self._ddl_account_type.click()
        self._opt_account_type(account_type).click()
        self._txt_deposit_initial.type(str(deposit_initial))
        self._btn_submit.click()

    def is_success_message_displayed(self) -> bool:
        return self._lbl_success_creation.is_element_displayed()

    def get_success_acount_messgae(self) -> str:
        return self._lbl_success_creation.get_text()

    def get_account_id(self) -> str:
        return self._account_info("Account ID").get_text()

    def get_customer_id(self) -> str:
        return self._account_info("Customer ID").get_text()

    def get_customer_name(self) -> str:
        return self._account_info("Customer Name").get_text()

    def get_email(self) -> str:
        return self._account_info("Email").get_text()

    def get_account_type(self) -> str:
        return self._account_info("Account Type").get_text()

    def get_date_opening(self) -> str:
        return self._account_info("Date of Opening").get_text()

    def get_current_amount(self) -> int:
        return int(self._account_info("Current Amount").get_text())
