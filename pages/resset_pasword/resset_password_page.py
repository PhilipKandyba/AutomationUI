from Base import Page
from Pages.RessetPasword.ResetPasswordPageLocators import ResetPasswordPageLocators


class ResetPasswordPage(Page):
    def is_reset_password_page_header(self):
        return self.is_displayed(ResetPasswordPageLocators.HEADER_RESET_PASSWORD)
