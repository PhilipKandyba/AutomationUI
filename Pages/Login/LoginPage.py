from Base import Page
from Pages.Login.LoginPageLocators import LoginPageLocators


class LoginPage(Page):
    def notification_from_email_field(self):
        element = self.driver.find_element(*LoginPageLocators.NOTIFICATION_EMPTY_EMAIL_FIELD)
        return element

    def notification_from_password_field(self):
        element = self.driver.find_element(*LoginPageLocators.NOTIFICATION_EMPTY_PASSWORD_FIELD)
        return element

    def form_notification(self):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(*LoginPageLocators.FORM_NOTIFICATION)
        return element

    def enter_email(self, email):
        self.driver.find_element(*LoginPageLocators.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.SUBMIT).click()

    def login_in(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
