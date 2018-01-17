from base import Page
from data import url
from pages.dashboard.dashboard_page_locators import DashboardPageLocators


class DashboardPage(Page):
    def click_intercom_open_chat_button(self):
        self.switch_to_frame(DashboardPageLocators.INTERCOM_IFRAME)
        self.click(DashboardPageLocators.INTERCOM_OPEN_CHAT_BUTTON)

    def is_statistic_header(self):
        return self.is_displayed(DashboardPageLocators.STATISTIC_HEADER)

    def is_intercom_opened_chat(self):
        self.switch_to_frame(DashboardPageLocators.INTERCOM_IFRAME)
        self.is_displayed(DashboardPageLocators.INTERCOM_CHAT)

    def is_intercom_frame(self):
        return self.is_displayed(DashboardPageLocators.INTERCOM_IFRAME)

    def text_currency_symbol(self):
        self.open_page(url.DASHBOARD)
        return self.get_text(DashboardPageLocators.CURRENCY_SYMBOL)
