import allure
from selenium.webdriver.common.by import By
from base import BaseAction


class PageLogin(BaseAction):
    username = By.XPATH, "text,请输入手机号码"
    password = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"
    # 显示密码按钮
    show_password_button = By.ID, "com.tpshop.malls:id/img_view_pwd"

    @allure.step(title="输入用户名")
    def input_username(self, text):
        # 在allure报告中解释说明
        allure.attach('用户名', text)
        self.input(self.username, text)

    @allure.step(title="输入密码")
    def input_password(self, text):
        allure.attach('密码' + text, "")
        self.input(self.password, text)

    @allure.step(title="点击登录按钮")
    def click_login(self):
        self.click(self.login_button)

    def is_feature_enabled_button(self):
        self.is_feature_enabled(self.login_button)

    def click_show_password(self):
        self.click(self.show_password_button)
