from selenium.webdriver.common.by import  By
from src.wrappers.element_wrapper import ElementWrapper
from src.wrappers.browser_wrapper import BrowserWrapper


class DeleteAccountPage:

    __instance = None
    _txt_account_id = ElementWrapper((By.XPATH, "//input[@name='accountno']"))
    _btn_submit = ElementWrapper((By.XPATH, "//input[@value='Submit']"))

    @staticmethod
    def get_instance():
        if DeleteAccountPage.__instance is None:
            DeleteAccountPage.__instance = DeleteAccountPage()
        return DeleteAccountPage.__instance

    def delete_account(self, account_id):
        self._txt_account_id.type(account_id)
        self._btn_submit.click()
        if BrowserWrapper.is_alert_displayed():
            # Handle to accept two alert
            BrowserWrapper.accept_alert()
            BrowserWrapper.accept_alert()
