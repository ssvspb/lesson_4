from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


def test_guest_should_see_add_product_to_basket_button(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket_button()
 
def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link) 
    page.open()
    page.add_product_to_basket()
#     page.solve_quiz_and_get_code()

def test_should_be_right_product_name_in_basket_message(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link) 
    page.open()
    product_name = page.get_product_name()
    page.add_product_to_basket()
    adding_product_name = page.get_adding_product_name()
    assert adding_product_name == product_name, "Wrong product name in adding to basket message"

def test_should_be_rigth_product_price_in_basket_message(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link) 
    page.open()
    page.add_product_to_basket()
    product_price = page.get_product_price()
    adding_product_price = page.get_adding_product_price()
    assert adding_product_price == product_price, "Wrong product name in adding to basket message"
