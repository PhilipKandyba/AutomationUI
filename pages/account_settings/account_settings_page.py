from base import Page
from pages.account_settings.account_settings_page_locators import AccountSettingsPageLocators


class AccountSettings(Page):
    def is_save_changes_button(self):
        return self.is_displayed(AccountSettingsPageLocators.SAVE_CHANGES_BUTTON)