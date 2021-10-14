from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        register_email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_ADDRESS_FIELD)
        register_email_field.send_keys(email)
        register_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        register_password_field.send_keys(password)
        register_password_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_FIELD)
        register_password_confirm_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "\"Login\" is not in current url"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
