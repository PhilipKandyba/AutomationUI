from base import Page
from data import url
from request.plugin_integration import plugin_diagnostic
from tools.mongodb import mongodb_last_user
from pages.login.login_page_locators import LoginPageLocators
from pages.header.header_element_locators import HeaderElementLocators


class LoginPage(Page):
    def open_login_page(self):
        self.open_page(url.LOGIN_PAGE)
        self.wait(10, LoginPageLocators.SUBMIT)

    def is_notification_from_email_field(self):
        return self.is_displayed(LoginPageLocators.NOTIFICATION_EMPTY_EMAIL_FIELD)

    def is_notification_from_password_field(self):
        return self.is_displayed(LoginPageLocators.NOTIFICATION_EMPTY_PASSWORD_FIELD)

    def text_notification_from_email_field(self):
        return self.get_text(LoginPageLocators.NOTIFICATION_EMPTY_EMAIL_FIELD)

    def text_notification_from_password_field(self):
        return self.get_text(LoginPageLocators.NOTIFICATION_EMPTY_PASSWORD_FIELD)

    def is_form_notification(self):
        self.driver.implicitly_wait(10)
        return self.is_displayed(LoginPageLocators.FORM_NOTIFICATION)

    def text_form_notification(self):
        self.driver.implicitly_wait(10)
        return self.get_text(LoginPageLocators.FORM_NOTIFICATION)

    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL, email)

    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD, password)

    def click_login_button(self):
        self.click(LoginPageLocators.SUBMIT)

    def click_link_forgot_password(self):
        self.click(LoginPageLocators.LINK_FORGOT_PASSWORD)

    def login_in(self, email=mongodb_last_user(), password='123456'):
        self.open_login_page()
        self.enter_email(email)
        print(email)
        self.enter_password(password)
        self.click_login_button()
        self.wait(500, HeaderElementLocators.LOGO_ICON)

    def is_login_button(self):
        return self.is_displayed(LoginPageLocators.SUBMIT)

    def plugin_integration(self):
        plugin_diagnostic()

