from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, feature):
        """
        根据某个特征，进行查找并且点击
        :param feature: 特征
        :return:
        """
        self.find_element(feature).click()

    def input(self, feature, text):
        """
        根据某个特征，进行查找并且输入对应的文字
        :param feature: 特征
        :param text: 文字
        :return:
        """
        self.find_element(feature).send_keys(text)

    def find_element(self, feature, timeout=5.0, poll=1.0):
        """
        根据特征，找元素
        :param feature: 特征
        :return: 元素
        """
        by = feature[0]
        value = feature[1]
        if by == By.XPATH:
            value = self.__make_xpath_with_feature(value)
            print(value)
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=5.0, poll=1.0):
        """
        根据特征，找元素
        :param feature: 特征
        :return: 元素
        """
        by = feature[0]
        value = feature[1]
        if by == By.XPATH:
            value = self.__make_xpath_with_feature(value)
            print(value)
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(by, value))

    @staticmethod
    def __make_xpath_with_unit_feature(xpath_value):
        """
        拼接xpath中间的部分
        :param loc:
        :return:
        """
        key_index = 0
        value_index = 1
        option_index = 2

        res_value = ""
        args = xpath_value.split(",")
        if len(args) == 3:
            if args[option_index] == "1":
                res_value += "@%s='%s' and " % (args[key_index], args[value_index])
            elif args[option_index] == "0":
                res_value += "contains(@%s,'%s') and " % (args[key_index], args[value_index])
        elif len(args) == 2:
            res_value += "contains(@%s,'%s') and " % (args[key_index], args[value_index])

        return res_value

    def __make_xpath_with_feature(self, xpath_value):

        xpath_start = "//*["
        xpath_end = "]"
        res_value = ""

        if isinstance(xpath_value, str):

            # 系统的xpath
            if xpath_value.startswith("/"):
                return xpath_value

            res_value = self.__make_xpath_with_unit_feature(xpath_value)

        elif isinstance(xpath_value, tuple):
            for i in xpath_value:
                res_value += self.__make_xpath_with_unit_feature(i)

        res_value = res_value.rstrip(" and ")

        res_value = xpath_start + res_value + xpath_end

        return res_value

    def find_toast(self, message, timeout=3):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位

        return self.find_element((By.XPATH, message), timeout=timeout, poll=0.1).text

    def is_toast_exist(self, message):
        """
        判断toast的部分消息是否存在
        :param message:
        :return:
        """
        try:
            self.find_toast(message)
            return True
        except Exception:
            return False

    def is_feature_enabled(self, feature):
        if self.find_element(feature).get_attribute("enabled") == "true":
            return True
        else:
            return False

    def is_feature_exist(self, feature):
        try:
            self.find_element(feature)
            return True
        except Exception:
            return False
