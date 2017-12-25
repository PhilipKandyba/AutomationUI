from Base import Page
from Pages.Dashboard.DashboardPageLocators import DashboardPageLocators


class DashboardPage(Page):
    def is_statistic_header(self):
        return self.is_displayed(DashboardPageLocators.STATISTIC_HEADER)