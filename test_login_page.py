from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators


def test_guest_can_go_to_login_page(browser):
    link = LoginPageLocators.LOGIN_URL
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_page()          # выполняем метод страницы — переходим на страницу логина

    