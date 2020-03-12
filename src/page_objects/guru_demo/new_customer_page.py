from __future__ import annotations
from selenium.webdriver.common.by import By
from src.wrappers.element_wrapper import ElementWrapper
from src.data_objects.customer import Customer

class NewCustomerPage:
    __instance = None

    # Locators
    _txt_customer_name = ElementWrapper((By.XPATH, "//input[@name='name']"))
    _txt_birthday = ElementWrapper((By.XPATH, "//input[@name='dob']"))
    _txa_address = ElementWrapper((By.XPATH, "//textarea[@name='addr']"))
    _txt_city = ElementWrapper((By.XPATH, "//input[@name='city']"))
    _txt_state = ElementWrapper((By.XPATH, "//input[@name='state']"))
    _txt_pin_number = ElementWrapper((By.XPATH, "//input[@name='pinno']"))
    _txt_phone_number = ElementWrapper((By.XPATH, "//input[@name='telephoneno']"))
    _txt_email_id = ElementWrapper((By.XPATH, "//input[@name='emailid']"))
    _txt_password = ElementWrapper((By.XPATH, "//input[@name='password']"))
    _btn_submit = ElementWrapper((By.XPATH, "//input[@value='Submit']"))
    _btn_reset = ElementWrapper((By.XPATH, "//input[@value='Reset']"))
    _lbl_success_creation = ElementWrapper((By.XPATH, "//table[@id='customer']//p[@class='heading3']"))

    # Dynamic controls
    def _customer_info(self, info_type: str) -> ElementWrapper:
        return ElementWrapper((By.XPATH, "//td[text()='{}']/following-sibling::td".format(info_type)))

    @staticmethod
    def get_instance():
        if NewCustomerPage.__instance is None:
            NewCustomerPage.__instance = NewCustomerPage()
        return NewCustomerPage.__instance

    def add_new_customer(self, customer_obj: Customer) -> None:
        # Fill all customer infos
        self._txt_customer_name.type(customer_obj.name)
        self._txt_birthday.type(customer_obj.birth_date)
        self._txa_address.type(customer_obj.address)
        self._txt_city.type(customer_obj.city)
        self._txt_state.type(customer_obj.state)
        self._txt_pin_number.type(customer_obj.pin)
        self._txt_phone_number.type(customer_obj.mobile_number)
        self._txt_email_id.type(customer_obj.email)
        self._txt_password.type(customer_obj.password)
        # Click submit
        self._btn_submit.click()

    def is_success_customer_creation_displayed(self) -> bool:
        return self._lbl_success_creation.is_element_displayed()

    def get_success_creation_label(self) -> str:
        return self._lbl_success_creation.get_text()

    def get_customer_id(self) -> str:
        return self._customer_info("Customer ID").get_text()

    def get_customer_name(self) -> str:
        return self._customer_info("Customer Name").get_text()

    def get_customer_gender(self) -> str:
        return self._customer_info("Gender").get_text()

    def get_customer_Birthdate(self) -> str:
        return self._customer_info("Birthdate").get_text()

    def get_customer_address(self) -> str:
        return self._customer_info("Address").get_text()

    def get_customer_city(self) -> str:
        return self._customer_info("City").get_text()

    def get_customer_state(self) -> str:
        return self._customer_info("State").get_text()

    def get_customer_pin(self) -> str:
        return self._customer_info("Pin").get_text()

    def get_customer_mobile_numer(self) -> str:
        return self._customer_info("Mobile No.").get_text()

    def get_customer_email(self) -> str:
        return self._customer_info("Email").get_text()
