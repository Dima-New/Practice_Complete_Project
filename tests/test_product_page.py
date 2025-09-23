from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(driver):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product = ProductPage(driver, url)
    product.open()
    product.add_to_basket()
    product.solve_quiz_and_get_code()
    product.check_product_name_in_message()
    product.check_product_price_in_basket()
