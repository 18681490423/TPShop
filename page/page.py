from .page_home import *
from .page_login import *
from .page_mine import *


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return PageHome(self.driver)

    @property
    def login(self):
        return PageLogin(self.driver)

    @property
    def mine(self):
        return PageMine(self.driver)
