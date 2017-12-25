from base import Page
from pages.login.login_page_locators import LoginPageLocators
from pages.setup.setup_page_locators import SetupPageLocators
from selenium.webdriver.common.by import By


class SetupPage(Page):
    def is_he_title(self):
        return self.is_displayed(SetupPageLocators.H2_TITLE)
