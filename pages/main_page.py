from .base_page import BasePage


class MainPage(BasePage):

    # calls the parent class constructor
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
