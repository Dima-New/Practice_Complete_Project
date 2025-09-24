from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.driver.find_element(
            *ProductPageLocators.ADD_TO_BASKET
        )
        add_to_basket_button.click()

    def check_product_name_in_message(self):
        product_name = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME)
        messsage = self.driver.find_element(*ProductPageLocators.SUCCESS_NAME)
        assert product_name.text == messsage.text, "product_name is not in message"

    def check_product_price_in_basket(self):
        price = self.driver.find_element(*ProductPageLocators.PRICE)
        basket = self.driver.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert price.text == basket.text, "price not equal to basket total"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is not disappeared, but should"
