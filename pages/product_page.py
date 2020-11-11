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
