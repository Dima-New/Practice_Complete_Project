from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.driver.current_url, "Login page does not appear in URL"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not present"

    def register_new_user(self, email, password):
        email_address = self.driver.find_element(
            *LoginPageLocators.REGISTER_EMAIL_INPUT
        )
        email_address.send_keys(email)
        password1 = self.driver.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        password1.send_keys(password)
        password2 = self.driver.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        password2.send_keys(password)
        register_button = self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
