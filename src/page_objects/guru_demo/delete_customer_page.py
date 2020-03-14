from selenium.webdriver.common.by import By
from src.wrappers.element_wrapper import ElementWrapper
from src.wrappers.browser_wrapper import BrowserWrapper


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

    def delete_customer(self, customer_id: str) -> None:
        self._txt_customer_id.type(customer_id)
        self._btn_submit.click()
        if BrowserWrapper.is_alert_displayed():
            # Handle to accept two alert
            BrowserWrapper.accept_alert()
            BrowserWrapper.accept_alert()
