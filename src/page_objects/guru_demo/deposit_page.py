from selenium.webdriver.common.by import By
from src.wrappers.element_wrapper import ElementWrapper


class DepositPage:

    __instance = None

    # Locators
    _txt_account_no = ElementWrapper((By.XPATH, "//input[@name='accountno']"))
    _txt_amount = ElementWrapper((By.XPATH, "//input[@name='ammount']"))
    _txt_description = ElementWrapper((By.XPATH, "//input[@name='desc']"))
    _btn_submit = ElementWrapper((By.XPATH, "//input[@name='AccSubmit']"))
    _lbl_success_deposit = ElementWrapper((By.XPATH, "//table[@id='deposit']//p[@class='heading3']"))

    # Dynamic controls
    def _deposit_info(self, info_kind: str) -> ElementWrapper:
        return ElementWrapper((By.XPATH, "//td[text()='{}']/following-sibling::td".format(info_kind)))

    @staticmethod
    def get_instance():
        if DepositPage.__instance is None:
            DepositPage.__instance = DepositPage()
        return DepositPage.__instance

    def add_new_deposit(self, account_id: str, amount: int, description: str) -> None:
        self._txt_account_no.type(account_id)
        self._txt_amount.type(str(amount))
        self._txt_description.type(description)
        self._btn_submit.click()

    def is_success_deposit_message_displayed(self) -> bool:
        return self._lbl_success_deposit.is_element_displayed()

    def get_success_deposit_mesaage(self) -> str:
        return self._lbl_success_deposit.get_text()

    def get_deposit_info(self, kind_of_info: str) -> str:
        # Argument 'kind_of_info' will get value from 'deposit_page_constants'
        return self._deposit_info(kind_of_info).get_text()
