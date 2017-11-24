from Base import Page
from Data import URL
from Pages.SignUp.SignupPageLocators import SignUpPageLocators
from Pages.SignUp.SignupPageLocators import select_industry
from Pages.SignUp.SignupPageLocators import selected_industry

class SignUpPage(Page):
    def open_signup_page(self):
        self.open_page(URL.SIGNUP_PAGE)

    def is_shop_url_field_required_massage(self):
        return self.is_displayed(SignUpPageLocators.SHOP_URL_FIELD_REQUIRED_MASSAGE)

    def is_email_field_required_massage(self):
        return self.is_displayed(SignUpPageLocators.EMAIL_FIELD_REQUIRED_MASSAGE)

    def is_password_field_required_massage(self):
        return self.is_displayed(SignUpPageLocators.PASSWORD_FIELD_REQUIRED_MASSAGE)

    def is_first_name_field_required_massage(self):
        return self.is_displayed(SignUpPageLocators.FIRST_NAME_FIELD_REQUIRED_MASSAGE)

    def click_signup_button(self):
        self.click(SignUpPageLocators.CONFIRMATION_BUTTON)

    def is_all_required_massage(self):
        self.click_signup_button()
        self.is_shop_url_field_required_massage()
        self.is_email_field_required_massage()
        self.is_first_name_field_required_massage()
        self.is_password_field_required_massage()

    def send_keys_shop_url_field(self, text):
        self.send_keys(SignUpPageLocators.SHOP_URL_FIELD, text)

    def send_keys_email_field(self, text):
        self.send_keys(SignUpPageLocators.EMAIL_FIELD, text)

    def send_keys_first_name_field(self, text):
        self.send_keys(SignUpPageLocators.FIRST_NAME_FIELD, text)

    def send_keys_password(self, text):
        self.send_keys(SignUpPageLocators.PASSWORD_FIELD, text)

    def chose_industry(self, industry_name):
        self.click(SignUpPageLocators.INDUSTRY_SELECT_BUTTON)
        return self.click(select_industry(industry_name))

    def is_selected_industry(self, industry_name):
        return self.is_displayed(selected_industry(industry_name))



