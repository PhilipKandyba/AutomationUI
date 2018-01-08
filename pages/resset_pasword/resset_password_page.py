from base import Page
from data import url
from pages.resset_pasword.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(Page):
    def is_reset_password_button( self ):
        return self.is_displayed(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)

    def open_password_page(self):
        self.open_page(url.RECOVERY_PASSWORD_PAGE)

    def click_reset_password_button(self):
        self.click(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)

    def is_email_field_error_massage(self):
        return self.is_displayed(ResetPasswordPageLocators.EMAIL_FIELD_ERROR_MASSAGE)

    def send_keys_email_field(self, text):
        self.send_keys(ResetPasswordPageLocators.EMAIL_FIELD, text)

    def send_keys_password_field(self, text):
        self.send_keys(ResetPasswordPageLocators.PASSWORD_FIELD, text)

    def text_email_field(self):
        return self.get_text(ResetPasswordPageLocators.EMAIL_FIELD_ERROR_MASSAGE)

    def text_of_notification(self):
        return self.get_text(ResetPasswordPageLocators.ERROR_NOTIFICATION)