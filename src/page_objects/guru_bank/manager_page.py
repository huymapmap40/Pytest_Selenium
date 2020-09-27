from __future__ import annotations
from selenium.webdriver.common.by import By
from src.wrappers.element_wrapper import ElementWrapper
from .new_customer_page import NewCustomerPage
from .new_account_page import NewAccountPage
from .deposit_page import DepositPage
from .delete_account_page import DeleteAccountPage
from .delete_customer_page import DeleteCustomerPage


class ManagerPage:

    __instance: ManagerPage = None

    # Init manager page element
    _mnu_new_customer = ElementWrapper((By.XPATH, "//ul[@class='menusubnav']/li/a[text()='New Customer']"))
    _mnu_new_account = ElementWrapper((By.XPATH, "//ul[@class='menusubnav']/li/a[text()='New Account']"))
    _mnu_deposit = ElementWrapper((By.XPATH, "//ul[@class='menusubnav']/li/a[text()='Deposit']"))
    _mnu_delete_account = ElementWrapper((By.XPATH, "//ul[@class='menusubnav']/li/a[text()='Delete Account']"))
    _mnu_delete_customer = ElementWrapper((By.XPATH, "//ul[@class='menusubnav']/li/a[text()='Delete Customer']"))

    @staticmethod
    def get_instance():
        if ManagerPage.__instance is None:
            ManagerPage.__instance = ManagerPage()
        return ManagerPage.__instance

    def go_to_new_customer_page(self) -> NewCustomerPage:
        self._mnu_new_customer.click()
        return NewCustomerPage.get_instance()

    def go_to_new_account_page(self) -> NewAccountPage:
        self._mnu_new_account.click()
        return NewAccountPage.get_instance()

    def go_to_deposit_page(self) -> DepositPage:
        self._mnu_deposit.click()
        return DepositPage.get_instance()

    def go_to_delete_account_page(self) -> DeleteAccountPage:
        self._mnu_delete_account.click()
        return DeleteAccountPage.get_instance()

    def go_to_delete_customer_page(self) -> DeleteCustomerPage:
        self._mnu_delete_customer.click()
        return DeleteCustomerPage.get_instance()
