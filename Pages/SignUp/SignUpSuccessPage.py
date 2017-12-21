from Base import Page
from Pages.SignUp.SignUpSuccessPageLocators import SignUpSuccessPageLocators
from Pages.SignUp.SignUpSuccessPageLocators import SignUpConfirmPageLocators


class SingUpSuccessPage(Page):
    def is_header(self):
        return self.is_displayed(SignUpSuccessPageLocators.HEADER)

    def is_confirm_header(self):
        return self.is_displayed(SignUpConfirmPageLocators.HEADER)

    def click_go_to_account_button(self):
        self.click(SignUpConfirmPageLocators.GO_TO_ACCOUNT_BUTTON)