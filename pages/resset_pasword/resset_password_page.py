from base import Page
from pages.resset_pasword.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(Page):
    def is_reset_password_page_header(self):
        return self.is_displayed(ResetPasswordPageLocators.HEADER_RESET_PASSWORD)
