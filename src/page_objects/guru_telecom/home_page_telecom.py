from selenium.webdriver.common.by import By
from src.wrappers.element_wrapper import ElementWrapper


class HomePageTelecom:

    __instance = None

    # Locators
    _txt_homepage_title = ElementWrapper((By.XPATH, "//span[@id='header']//a[text()='Guru99 telecom']"))

    @staticmethod
    def get_instance():
        if HomePageTelecom.__instance is None:
            HomePageTelecom.__instance = HomePageTelecom()
        return HomePageTelecom.__instance

    def is_homepage_title_displayed(self) -> bool:
        return self._txt_homepage_title.is_element_displayed()
