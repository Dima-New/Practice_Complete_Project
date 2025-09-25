import pytest
import time

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


@pytest.mark.need_review
@pytest.mark.parametrize(
    "url",
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail,
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
    ],
)
def test_guest_can_add_product_to_basket(driver, url):
    product = ProductPage(driver, url)
    product.open()
    product.add_to_basket()
    product.solve_quiz_and_get_code()
    product.check_product_name_in_message()
    product.check_product_price_in_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(driver, url)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(driver, url)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(driver, url)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappeared()


def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, url)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, url)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.product_is_not_in_basket()
    basket_page.is_basket_empty()


@pytest.mark.user_add_product_to_basket
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        registration = LoginPage(driver, url)
        registration.open()
        registration.register_new_user(
            email=str(time.time()) + "test@mail.com", password="test12345$"
        )
        registration.should_be_authorized_user()

    def test_user_cant_see_success_message(self, driver):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(driver, url)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product = ProductPage(driver, url)
        product.open()
        product.add_to_basket()
        product.check_product_name_in_message()
        product.check_product_price_in_basket()
