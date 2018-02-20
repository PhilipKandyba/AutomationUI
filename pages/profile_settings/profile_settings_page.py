from base import Page
from data import url
from tools.mongodb import mongodb_last_user
from tools.postgresql import get_user_data
from pages.profile_settings.profile_settings_page_locators import ProfileSettingsPageLocators


class ProfileSettings(Page):
    def open_profile_settings_page(self):
        self.open_page(url.PROFILE_SETTINGS)
        self.wait(10, ProfileSettingsPageLocators.HEADER)

    def is_profile_settings_header(self):
        return self.is_displayed(ProfileSettingsPageLocators.HEADER)

    def is_disabled_save_changes_button(self):
        return self.is_displayed(ProfileSettingsPageLocators.DISABLED_SAVE_CHANGES_BUTTON)

    def text_first_name_field_notification(self):
        return self.get_text(ProfileSettingsPageLocators.FIRST_NAME_FIELD_ERROR_NOTIFICATION)

    def text_last_name_field_notification(self):
        return self.get_text(ProfileSettingsPageLocators.LAST_NAME_FIELD_ERROR_NOTIFICATION)

    def text_current_password_field_notification(self):
        return self.get_text(ProfileSettingsPageLocators.NEW_PASSWORD_FIELD_ERROR_NOTIFICATION)

    def text_new_password_field_notification(self):
        return self.get_text(ProfileSettingsPageLocators.CURRENT_PASSWORD_FIELD_ERROR_NOTIFICATION)

    def text_error_notification(self):
        return self.get_text(ProfileSettingsPageLocators.NOTIFICATION_ERROR)

    def value_first_name(self):
        return self.get_value(ProfileSettingsPageLocators.FIRST_NAME_FIELD)

    def value_last_name(self):
        return self.get_value(ProfileSettingsPageLocators.LAST_NAME_FIELD)

    def value_email(self):
        return self.get_value(ProfileSettingsPageLocators.EMAIL_FIELD)

    def send_keys_first_name_field(self, text):
        self.send_keys(ProfileSettingsPageLocators.FIRST_NAME_FIELD, text)

    def send_keys_last_name_field(self, text):
        self.send_keys(ProfileSettingsPageLocators.LAST_NAME_FIELD, text)

    def send_keys_current_password(self, text):
        self.send_keys(ProfileSettingsPageLocators.CURRENT_PASSWORD_FIELD, text)

    def send_keys_new_password(self, text):
        self.send_keys(ProfileSettingsPageLocators.NEW_PASSWORD_FIELD, text)

    def click_save_disabled_changes_button(self):
        self.click(ProfileSettingsPageLocators.DISABLED_SAVE_CHANGES_BUTTON)

    def click_save_changes_button(self):
        self.click(ProfileSettingsPageLocators.SAVE_CHANGES_BUTTON)

    def clear_first_name_field(self):
        self.clear_field(ProfileSettingsPageLocators.FIRST_NAME_FIELD)

    def clear_last_name_field(self):
        self.clear_field(ProfileSettingsPageLocators.LAST_NAME_FIELD)

    def clear_current_password_field(self):
        self.clear_field(ProfileSettingsPageLocators.CURRENT_PASSWORD_FIELD)

    def clear_new_password_field(self):
        self.clear_field(ProfileSettingsPageLocators.NEW_PASSWORD_FIELD)

    def check_first_name_in_db(self, email=mongodb_last_user()):
        user_name, api_key, shop_url, shop_currency, first_name, esp_email_from, support_email = get_user_data(email)
        return first_name