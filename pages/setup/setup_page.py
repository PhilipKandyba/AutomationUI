from base import Page
from data import url
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

    def text_he_title(self):
        return self.get_text(SetupPageLocators.H2_TITLE)

    def click_sign_up_next_step_button(self):
        self.click(SetupPageLocators.SIGN_UP_NEXT_STEP_BUTTON)

    def click_sign_up_popup_button(self):
        self.click(SetupPageLocators.SIGN_UP_POPUP_BUTTON)

    def click_sign_up_settings_link(self):
        self.click(SetupPageLocators.SIGN_UP_SETTINGS_LINK)

    def click_integration_open_cms_list(self):
        self.click(SetupPageLocators.INTEGRATION_OPEN_CMS_LIST)

    def click_integration_download_plugin_button(self):
        self.click(SetupPageLocators.INTEGRATION_DOWNLOAD_PLUGIN_BUTTON)
        self.switch_to_open_window()

    def click_integration_send_instruction_button(self):
        self.click(SetupPageLocators.INTEGRATION_SEND_INSTRUCTION_BUTTON)

    def click_integration_watch_tutorial_link(self):
        self.click(SetupPageLocators.INTEGRATION_WATCH_TUTORIAL_LINK)
        self.switch_to_open_window()

    def click_integration_send_instruction_to_developer_button(self):
        self.click(SetupPageLocators.INTEGRATION_SEND_INSTRUCTION_FORM_SEND_BUTTON)

    def enter_developer_email(self, email):
        self.send_keys(SetupPageLocators.INTEGRATION_SEND_INSTRUCTION_FORM_INPUT, email)

    def choose_cms(self, name):
        self.click_integration_open_cms_list()
        self.click(select_cms(name))

    def open_setup_sign_up_page(self):
        self.open_page(url.SETUP_SIGN_UP)

    def open_setup_integration_page(self):
        self.open_page(url.SETUP_INTEGRATION)

    def is_integration_api_url_label( self ):
        return self.is_displayed(SetupPageLocators.INTEGRATION_API_ULR_LABEL)