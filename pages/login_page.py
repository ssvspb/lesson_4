from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        exp_text = "login"
        page_url = self.browser.current_url
        assert exp_text in page_url, f"No '{exp_text}' in '{page_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "User email field is not presented in login page"
        user_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        user_email.send_keys(email)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Password1 field is not presented in login page"
        registration_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        registration_password1.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Password2 field is not presented in login page"
        registration_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        registration_password2.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Registration submit is not presented in login page"
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_submit.click()
        
             
