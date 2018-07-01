from selenium.webdriver.common.by import By
from base import BaseAction


class PageLogin(BaseAction):
    username = By.XPATH, "text,请输入手机号码"
    password = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_text(self):
        self.input(self.username, "18681490423")
        self.input(self.password, "123456")
        self.click(self.login_button)


