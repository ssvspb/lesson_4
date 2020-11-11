from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest
import time

@pytest.mark.skip("True")
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
@pytest.mark.parametrize('link', links[:])
def test_guest_can_add_product_to_basket(browser, link):
#     link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link) 
    page.open()
    product_name = page.get_product_name()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    adding_product_name = page.get_adding_product_name()
    assert adding_product_name == product_name, "Wrong product name in adding to basket message"

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
