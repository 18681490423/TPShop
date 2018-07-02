from selenium.webdriver.common.by import By
from base import BaseAction


class PageLogin(BaseAction):
    username = By.XPATH, "text,请输入手机号码"
    password = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_username(self, text):
        self.input(self.username, text)

    def input_password(self, text):
        self.input(self.password, text)

    def click_login(self):
        self.click(self.login_button)


