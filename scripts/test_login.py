from base import init_driver
from page import Page


class TestLogin:
    driver = None
    page = None

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # def test_home(self):
    #     self.page.home.click_mine()

    def test_login(self):
        # 点击我的按钮
        self.page.home.click_mine()
        # 点击登录/注册
        self.page.mine.click_login_signup()
        # 输入用户名和密码,点击登录
        self.page.login.input_text()
        # 断言
        # self.page.login.is_toast_exist("登录成功")
        assert "登录成功" == self.page.login.find_toast("登录成功")


