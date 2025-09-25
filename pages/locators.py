from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "input#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div#messages div.alertinner:last-child p strong")
    PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    SUCCESS_NAME = (By.CSS_SELECTOR, "div#messages div.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alertinner")


class BasketPageLocators:
    BASKET_SUMMARY = (By.CSS_SELECTOR, "form.basket_summary")
    EMPTY_BASKET = (By.CSS_SELECTOR, "div#content_inner p")
