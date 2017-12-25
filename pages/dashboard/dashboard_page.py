from base import Page
from pages.dashboard.dashboard_page_locators import DashboardPageLocators


class DashboardPage(Page):
    def is_statistic_header(self):
        return self.is_displayed(DashboardPageLocators.STATISTIC_HEADER)