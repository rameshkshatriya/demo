from selenium.webdriver.common.by import By

from features.pages.basepage import basepage


class accountsuccesspage(basepage):

    def __init__(self,driver):
        super().__init__(driver)

    account_success_heading_xpath = "//div[@id = 'content']/h1"

    def register_account_success(self,created_text):
        self.reterive_element_text_equals("account_success_heading_xpath",self.account_success_heading_xpath,created_text)
        # self.driver.find_element(By.XPATH, self.account_success_heading_xpath).text.__eq__(created_text)