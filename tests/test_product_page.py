import pytest

from pages.product_page import ProductPage


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


def test_message_disappeared_after_adding_product_to_basket(driver):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(driver, url)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappeared()
