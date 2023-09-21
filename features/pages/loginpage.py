from selenium.webdriver.common.by import By

from features.pages.accountpage import accountpage
from features.pages.basepage import basepage


class loginpage(basepage):

    def __init__(self,driver):
        super().__init__(driver)

    email_fields_xpath = "//div/div/form/div[1]/input[@id='input-email']"
    password_fields_xpath = "//div/div/form/div[2]/input[@id='input-password']"
    login_button_xpath = "//div/div/form/input[@type='submit']"
    proper_warning_message_xpath = "//div/div[text()='Warning: No match for E-Mail Address and/or Password.']"

    def send_email_text(self,email_text):
        self.type_into_element("email_fields_xpath",self.email_fields_xpath,email_text)
        # self.driver.find_element(By.XPATH, self.email_fields_xpath).send_keys(email_text)

    def send_password_text(self,passwd_text):
        self.type_into_element("password_fields_xpath",self.password_fields_xpath,passwd_text)
        # self.driver.find_element(By.XPATH, self.password_fields_xpath).send_keys(passwd_text)

    def click_login_button(self):
        self.click_on_element("login_button_xpath",self.login_button_xpath)
        # self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return accountpage(self.driver)

    def proper_warning_message(self,warning_message):
        self.reterive_element_text_contains('proper_warning_message_xpath',self.proper_warning_message_xpath,warning_message)
        # self.driver.find_element(By.XPATH, self.proper_warning_message_xpath).text.__contains__(warning_message)
