from base import Page
from pages.header.header_element_locators import HeaderElementLocators


class HeaderElement(Page):
    def click_logo(self):
        self.click(HeaderElementLocators.IMG_LOGO)

    def click_login_link(self):
        self.click(HeaderElementLocators.LINK_LOGIN_IN)

    def click_sign_up_link(self):
        self.click(HeaderElementLocators.LINK_SIGN_UP)