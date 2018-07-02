import pytest
from base import analyze_data
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

    @pytest.mark.parametrize("args", analyze_data("test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        expect = args["expect"]

        # 点击我的按钮
        self.page.home.click_mine()
        # 点击登录/注册
        self.page.mine.click_login_signup()
        # 输入用户名和密码,点击登录
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        self.page.login.click_login()
        # 判断toast是否和数据中的expect一致
        assert self.page.login.is_toast_exist(expect)
        # self.page.login.is_toast_exist("登录成功")
        # assert "登录成功" == self.page.login.find_toast("登录成功")




