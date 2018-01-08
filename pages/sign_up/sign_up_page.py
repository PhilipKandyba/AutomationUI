from base import Page
from data import url
from data.industry import INDUSTRY
from tools.mongodb import mongodb_insert_user
from pages.sign_up.sign_up_page_locators import SignUpPageLocators
from pages.sign_up.sign_up_page_locators import select_industry
from pages.sign_up.sign_up_page_locators import selected_industry


class SignUpPage(Page):
    def open_signup_page(self):
        self.open_page(url.SIGNUP_PAGE)

    def is_shop_url_field_required_massage(self):
        return self.is_displayed(SignUpPageLocators.SHOP_URL_FIELD_ERROR_MASSAGE)

    def is_email_field_required_massage(self):
        return self.is_displayed(SignUpPageLocators.EMAIL_FIELD_ERROR_MASSAGE)

    def is_password_field_required_massage(self):
        return self.is_displayed(SignUpPageLocators.PASSWORD_FIELD_ERROR_MASSAGE)

    def is_first_name_field_required_massage(self):
        return self.is_displayed(SignUpPageLocators.FIRST_NAME_FIELD_ERROR_MASSAGE)

    def is_industry_field_required_massage(self):
        return self.is_displayed(SignUpPageLocators.INDUSTRY_FIELD_ERROR_MASSAGE)

    def is_sign_up_button(self):
        return self.is_displayed(SignUpPageLocators.CONFIRMATION_BUTTON)

    def text_shop_url_field_error_massage(self):
        return self.get_text(SignUpPageLocators.SHOP_URL_FIELD_ERROR_MASSAGE)

    def text_email_field_error_massage(self):
        return self.get_text(SignUpPageLocators.EMAIL_FIELD_ERROR_MASSAGE)

    def text_first_name_field_error_massage(self):
        return self.get_text(SignUpPageLocators.FIRST_NAME_FIELD_ERROR_MASSAGE)

    def text_password_field_error_massage(self):
        return self.get_text(SignUpPageLocators.PASSWORD_FIELD_ERROR_MASSAGE)

    def click_signup_button(self):
        self.click(SignUpPageLocators.CONFIRMATION_BUTTON)

    def is_all_required_massage(self):
        self.click_signup_button()
        self.is_shop_url_field_required_massage()
        self.is_industry_field_required_massage()
        self.is_first_name_field_required_massage()
        self.is_email_field_required_massage()
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
        self.implicitly_wait(10)
        self.click(select_industry(industry_name))

    def is_selected_industry(self, industry_name):
        return self.is_displayed(selected_industry(industry_name))

    def text_of_notification(self):
        return self.get_text(SignUpPageLocators.ERROR_NOTIFICATION)

    def fill_the_form(self, shop, email, name, password, industry=INDUSTRY[1]):
        self.send_keys_shop_url_field(shop)
        self.send_keys_email_field(email)
        self.send_keys_first_name_field(name)
        self.send_keys_password(password)
        self.chose_industry(industry)

    def new_registration(self, shop, email, name, password, industry):
        self.fill_the_form(shop, email, name, password, industry)
        self.click_signup_button()
        mongodb_insert_user(email, name, password, industry, shop)

    def click_terms_of_use(self):
        self.click(SignUpPageLocators.LINK_TERMS_OF_USE)

    def click_privacy_policy(self):
        self.click(SignUpPageLocators.LINK_PRIVACY_POLICY)

    def text_terms_of_use_header(self):
        self.switch_to_open_window()
        return self.get_text(SignUpPageLocators.HEADER_TERMS_OF_USE)

    def text_privacy_policy_header(self):
        self.switch_to_open_window()
        return self.get_text(SignUpPageLocators.HEADER_PRIVACY_POLICY)

    def check_industry_list(self, ind):
        for i in ind:
            try:
                print(i)
                self.chose_industry(i)
                assert self.is_selected_industry(i)
            except:
                raise Exception('Industry ' + i + ' not found')

