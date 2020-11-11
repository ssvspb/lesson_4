from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators


def test_guest_can_go_to_login_page(browser):
    link = LoginPageLocators.LOGIN_PAGE_URL
    page = LoginPage(browser, link) 
    page.open()
    page.should_be_login_page()

    