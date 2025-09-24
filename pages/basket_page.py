from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_empty(self):
        basket_message = self.driver.find_element(*BasketPageLocators.EMPTY_BASKET)
        assert (
            basket_message.text == "Your basket is empty. Continue shopping"
        ), "basket is not empty"

    def product_is_not_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_SUMMARY
        ), "product in basket"
