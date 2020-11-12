from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
import pytest
import time

# @pytest.mark.skip("True")
def test_guest_should_see_add_product_to_basket_button(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket_button()

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
 pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
# @pytest.mark.skip("True")
@pytest.mark.parametrize('link', links[:1])
def test_guest_can_add_product_to_basket(browser, link):
#     link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link) 
    page.open()
    product_name = page.get_product_name()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    adding_product_name = page.get_adding_product_name()
    assert adding_product_name == product_name, "Wrong product name in adding to basket message"
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
@pytest.mark.skip("True")
def test_should_be_right_product_name_in_basket_message(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link) 
    page.open()
    product_name = page.get_product_name()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    adding_product_name = page.get_adding_product_name()
    assert adding_product_name == product_name, "Wrong product name in adding to basket message"


@pytest.mark.skip("True")
def test_should_be_rigth_product_price_in_basket_message(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link) 
    page.open()
    product_price = page.get_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    adding_product_price = page.get_adding_product_price()
    assert adding_product_price == product_price, "Wrong product name in adding to basket message"

@pytest.mark.skip("True")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link) 
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    
# @pytest.mark.skip("True")
def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link) 
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip("True")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link) 
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_message()
    