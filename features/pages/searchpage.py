from selenium.webdriver.common.by import By

from features.pages.basepage import basepage


class searchpage(basepage):

    def __init__(self,driver):
        super().__init__(driver)

    valid_product_link_text = "iPhone"
    warning_message_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_product(self):
        self.display_status("valid_product_link_text",self.valid_product_link_text)
        # self.driver.find_element(By.LINK_TEXT, self.valid_product_link_text).is_displayed()

    def invalid_product_warning_message(self,expected_message_text):
        self.reterive_element_text_equals("warning_message_xpath",self.warning_message_xpath,expected_message_text)
        # self.driver.find_element(By.XPATH, self.warning_message_xpath).text.__eq__(expected_message_text)