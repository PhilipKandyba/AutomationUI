import re
from base import Page
from data import url
from tools.mongodb import mongodb_last_user
from tools.postgresql import get_user_data
from pages.setup.setup_page_locators import select_cms
from pages.setup.setup_page_locators import SetupPageLocators


class SetupPage(Page):
    def is_he_title(self):
        return self.is_displayed(SetupPageLocators.H2_TITLE)

    def is_popup_title(self):
        try:
            return self.is_displayed(SetupPageLocators.SIGN_UP_POPUP_TITLE)
        finally:
            self.click_sign_up_popup_button()

    def click_sign_up_next_step_button(self):
        self.click(SetupPageLocators.SIGN_UP_NEXT_STEP_BUTTON)

    def click_sign_up_popup_button(self):
        self.click(SetupPageLocators.SIGN_UP_POPUP_BUTTON)

    def click_sign_up_settings_link(self):
        self.click(SetupPageLocators.SIGN_UP_SETTINGS_LINK)

    def click_integration_open_cms_list(self):
        self.click(SetupPageLocators.INTEGRATION_OPEN_CMS_LIST_BUTTON)

    def click_integration_download_plugin_button(self):
        self.click(SetupPageLocators.INTEGRATION_DOWNLOAD_PLUGIN_BUTTON)
        self.close_first_windows()
        self.switch_to_open_window()

    def click_integration_send_instruction_button(self):
        self.click(SetupPageLocators.INTEGRATION_SEND_INSTRUCTION_BUTTON)

    def click_integration_watch_tutorial_link(self):
        self.click(SetupPageLocators.INTEGRATION_WATCH_TUTORIAL_LINK)
        self.close_first_windows()
        self.switch_to_open_window()

    def click_integration_send_instruction_to_developer_button(self):
        self.click(SetupPageLocators.INTEGRATION_SEND_INSTRUCTION_FORM_SEND_BUTTON)

    def click_integration_confirm_shop_details_button(self):
        self.click(SetupPageLocators.INTEGRATION_CONFIRM_SHOP_DETAILS_BUTTON)

    def send_keys_developer_email(self, email=mongodb_last_user()):
        self.send_keys(SetupPageLocators.INTEGRATION_SEND_INSTRUCTION_FORM_INPUT, email)

    def send_keys_shop_url(self, shop_url):
        self.send_keys(SetupPageLocators.INTEGRATION_SHOP_URL_INPUT, shop_url)

    def choose_cms(self, name):
        self.click_integration_open_cms_list()
        self.click(select_cms(name))
        self.wait_until_element_is_not_show(30, SetupPageLocators.INTEGRATION_CMS_LIST)

    def open_setup_sign_up_page(self):
        self.open_page(url.SETUP_SIGN_UP)

    def open_setup_integration_page(self):
        self.open_page(url.SETUP_INTEGRATION)

    def is_integration_api_url_label(self):
        return self.is_displayed(SetupPageLocators.INTEGRATION_API_ULR_LABEL)

    def text_he_title(self):
        return self.get_text(SetupPageLocators.H2_TITLE)

    def text_cms_name_tutorial_block(self):
        cms = self.get_text(SetupPageLocators.INTEGRATION_CMS_NAME_TUTORIAL_BLOCK)
        print(cms[23:-4])
        return cms[23:-4]

    def text_cms_name_credential_block(self):
        cms = self.get_text(SetupPageLocators.INTEGRATION_CMS_NAME_CREDENTIAL_BLOCK)
        print(cms[54:])
        return cms[54:]

    def text_send_instruction_form_error_massage(self):
        return self.get_text(SetupPageLocators.INTEGRATION_SEND_INSTRUCTION_FORM_ERROR_MASSAGE)

    def text_of_notification_massage(self):
        return self.get_text(SetupPageLocators.SETUP_NOTIFICATION_MASSAGE)

    def text_of_plugin_status_block(self):
        return self.get_text(SetupPageLocators.INTEGRATION_PLUGIN_STATUS_BLOCK)

    def value_of_api_url(self):
        return self.get_value(SetupPageLocators.INTEGRATION_API_URL_INPUT)

    def value_of_api_key(self):
        return self.get_value(SetupPageLocators.INTEGRATION_API_KEY_INPUT)

    def value_shop_url(self):
        return self.get_value(SetupPageLocators.INTEGRATION_SHOP_URL_INPUT)

    def check_api_key_db(self, email=mongodb_last_user()):
        api_key, user_name, shop_url = get_user_data(email)
        return api_key

    def check_shop_url_in_db(self, email=mongodb_last_user()):
        api_key, user_name, shop_url = get_user_data(email)
        return shop_url
