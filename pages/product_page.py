from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    def should_be_add_product_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
     
    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
        
    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented in page"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name
    
    def get_adding_product_name(self):
        assert self.is_element_present(*ProductPageLocators.ADDING_PRODUCT_NAME), "Product name is not presented in adding to basket message"
        product_name = self.browser.find_element(*ProductPageLocators.ADDING_PRODUCT_NAME).text
        return product_name
    
    def get_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented in page"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price
    
    def get_adding_product_price(self):
        assert self.is_element_present(*ProductPageLocators.ADDING_PRODUCT_PRICE), "Product price is not presented in adding to basket message"
        product_price = self.browser.find_element(*ProductPageLocators.ADDING_PRODUCT_PRICE).text
        return product_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"
            
    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should be diappeared"
            
    def should_be_right_product_name_in_adding_to_basket_message(self):
        product_name = self.get_product_name()
        adding_product_name = self.get_adding_product_name()
        assert adding_product_name == product_name, "Wrong product name in adding to basket message"

    def should_be_right_product_price_in_adding_to_basket_message(self):
        product_price = self.get_product_price()
        adding_product_price = self.get_adding_product_price()
        assert adding_product_price == product_price, "Wrong product price in adding to basket message"
        