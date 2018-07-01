from selenium.webdriver.common.by import By

from base import BaseAction


class PageHome(BaseAction):
    mine_button = By.XPATH, "text,我的", "resource-id,com.tpshop.malls:id/tab_txtv"

    def click_mine(self):
        self.click(self.mine_button)