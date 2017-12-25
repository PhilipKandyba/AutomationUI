from Base import Page
from Pages.Login.LoginPageLocators import LoginPageLocators
from Pages.Setup.SetupPageLocators import SetupPageLocators
from selenium.webdriver.common.by import By


class SetupPage(Page):
    def is_he_title(self):
        return self.is_displayed(SetupPageLocators.H2_TITLE)
