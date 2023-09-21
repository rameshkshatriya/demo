from selenium.webdriver.common.by import By

from features.pages.basepage import basepage


class accountpage(basepage):

    def __init__(self,driver):
        super().__init__(driver)

    edit_your_account_xpath = "//div/ul/li[1]/a[text()='Edit your account information']"

    def edit_account_information(self):
        self.display_status("edit_your_account_xpath",self.edit_your_account_xpath)
        # self.driver.find_element(By.XPATH , self.edit_your_account_xpath).is_displayed()