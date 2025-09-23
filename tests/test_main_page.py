from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(driver):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(driver):
    url = "http://selenium1py.pythonanywhere.com"
    page = MainPage(driver, url)
    page.open()
    assert page.should_be_login_link(), "Login link is not presented"
