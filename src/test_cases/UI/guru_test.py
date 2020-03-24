from hamcrest import assert_that, equal_to
from src.page_objects.guru_demo import *
from src.test_data.general.page_urls import PageUrls
from src.data_objects.customer import Customer
from src.wrappers.browser_wrapper import BrowserWrapper
from src.data_objects.page_constants.deposit_page_constants import DepositPageConstants
from ..TestBase import TestBase


class TestGuru(TestBase):
    # Declare parameters
    access_email = "huymapmap40@gmail.com"
    user_id = ""
    user_passwd = ""
    customer_name = "Test name"
    customer_gender = "male"
    customer_birthday = "01031994"
    customer_address = "Test Address"
    customer_city = "ho chi minh"
    customer_state = "StateABCXYZ"
    customer_pin = "123456"
    customer_phone = "654321"
    customer_email = "huymapmap@gmail.com"
    customer_passwd = "123456"
    message_customer_added = "Customer Registered Successfully!!!"
    message_account_created = "Account Generated Successfully!!!"
    message_deposit_transaction = "Transaction details of Deposit for Account"
    account_type = "Savings"
    deposit_init = 1000
    extra_deposit = 2000
    desc_deposit = "Add"

    def test_guru_functional(self):
        print("==== Start test guru99 functional ====")
        TestGuru.setup_test(PageUrls.GURU_99_PAGE)
        fill_email_obj = FillEmailGuruPage.get_instance()

        # Fill an email and get username/passwd
        fill_email_obj.fill_email_and_submit(self.access_email)
        user_id = fill_email_obj.get_user_name()
        user_passwd = fill_email_obj.get_password()

        # Login to manager page with valid authentication
        browser_obj = BrowserWrapper()
        browser_obj.go_to_url(PageUrls.LOGIN_GURU_99_PAGE)
        login_page_obj = LoginPage.get_instance()
        manager_page_obj = login_page_obj.login_to_manager_page(user_id, user_passwd)

        # Add new customer
        new_customer_page_obj = manager_page_obj.go_to_new_customer_page()
        customer_obj = Customer(self.customer_name, self.customer_birthday, self.customer_address,
                                self.customer_city, self.customer_state, self.customer_pin, self.customer_phone,
                                self.customer_email, self.customer_passwd)
        new_customer_page_obj.add_new_customer(customer_obj)
        customer_id = new_customer_page_obj.get_customer_id()
        print("=====> Customer ID: {}".format(customer_id))

        # VP: New customer is added
        assert_that(new_customer_page_obj.is_success_customer_creation_displayed(), equal_to(True))
        assert_that(new_customer_page_obj.get_customer_name(), self.customer_name)
        assert_that(new_customer_page_obj.get_customer_address(), self.customer_address)
        assert_that(new_customer_page_obj.get_customer_city(), self.customer_city)
        assert_that(new_customer_page_obj.get_customer_email(), self.customer_email)
        assert_that(new_customer_page_obj.get_customer_gender(), self.customer_gender)
        assert_that(new_customer_page_obj.get_customer_state(), self.customer_state)
        assert_that(new_customer_page_obj.get_customer_pin(), self.customer_pin)
        assert_that(new_customer_page_obj.get_customer_mobile_numer(), self.customer_phone)
        assert_that(new_customer_page_obj.get_success_creation_label(), self.message_customer_added)
        # assert_that(new_customer_page_obj.get_customer_name(), self.customer_name)

        # Add new account
        new_account_page_obj = manager_page_obj.go_to_new_account_page()
        new_account_page_obj.add_new_account(customer_id, self.account_type, self.deposit_init)
        account_id = new_account_page_obj.get_account_id()
        current_amount = new_account_page_obj.get_current_amount()
        print("=====> Account ID: {}".format(account_id))

        # VP: New account is added
        assert_that(new_account_page_obj.is_success_message_displayed(), equal_to(True))
        assert_that(new_account_page_obj.get_success_acount_messgae(), self.message_account_created)
        assert_that(new_account_page_obj.get_customer_name(), self.customer_name)
        assert_that(new_account_page_obj.get_account_type(), self.account_type)
        assert_that(new_account_page_obj.get_email(), self.customer_email)
        assert_that(current_amount, str(self.deposit_init))
        assert_that(new_account_page_obj.get_customer_id(), customer_id)

        # Add new deposit
        deposit_page_obj = manager_page_obj.go_to_deposit_page()
        deposit_page_obj.add_new_deposit(account_id, self.extra_deposit, self.desc_deposit)

        # VP: New deposit is added
        assert_that(deposit_page_obj.is_success_deposit_message_displayed(), equal_to(True))
        assert_that(deposit_page_obj.get_deposit_info(DepositPageConstants.ACCOUNT_ID), account_id)
        assert_that(deposit_page_obj.get_deposit_info(DepositPageConstants.AMOUNT_CREDITED), str(self.extra_deposit))
        assert_that(deposit_page_obj.get_deposit_info(DepositPageConstants.TRANSACTION_TYPE), "Deposit")
        assert_that(deposit_page_obj.get_deposit_info(DepositPageConstants.DESCRIPTION), self.desc_deposit)
        assert_that(deposit_page_obj.get_deposit_info(DepositPageConstants.CURRENT_BALANCE), str(current_amount +
                                                                                                 self.extra_deposit))

        # Cleanup
        delete_account_page_obj = manager_page_obj.go_to_delete_account_page()
        delete_account_page_obj.delete_account(account_id)
        delete_customer_page_obj = manager_page_obj.go_to_delete_customer_page()
        delete_customer_page_obj.delete_customer(customer_id)
        TestGuru.cleanup_test()
