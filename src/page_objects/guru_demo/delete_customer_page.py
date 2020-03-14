from selenium.webdriver.common.by import By
from src.wrappers.element_wrapper import ElementWrapper, BrowserWrapper


class DeleteCustomerPage:
    __instance = None

    # Locators
    _txt_customer_id = ElementWrapper((By.XPATH, "//input[@name='cusid']"))
    _btn_submit = ElementWrapper((By.XPATH, "//input[@value='Submit']"))

    @staticmethod
    def get_instance():
        if DeleteCustomerPage.__instance is None:
            DeleteCustomerPage.__instance = DeleteCustomerPage()
        return DeleteCustomerPage.__instance

    def deleteC_customer(self, customer_id: str) -> None:
        self._txt_customer_id.type(customer_id)
        self._btn_submit.click()
        if BrowserWrapper.is_alert_displayed():
            BrowserWrapper.accept_alert()
