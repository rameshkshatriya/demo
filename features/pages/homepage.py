from selenium.webdriver.common.by import By

from features.pages.basepage import basepage
from features.pages.loginpage import loginpage
from features.pages.registerpage import registerpage
from features.pages.searchpage import searchpage


class homepage(basepage):

    def __init__(self,driver):
        super().__init__(driver)

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_xpath = "//div/div[2]/ul/li[2]/ul/li[2]/a[text()='Login']"
    search_field_xpath = "//div[@id = 'search']/input[@name='search']"
    click_on_button_xpath = "//div/span/button[@type='button']"
    register_option_xpath = "//div/ul/li[2]/ul/li[1]/a[text()='Register']"

    def click_on_my_account(self):
        self.click_on_element("my_account_option_xpath",self.my_account_option_xpath)
        # self.driver.find_element(By.XPATH, self.my_account_option_xpath).click()

    def click_on_login(self):
        self.click_on_element("login_option_xpath",self.login_option_xpath)
        # self.driver.find_element(By.XPATH, self.login_option_xpath).click()
        return loginpage(self.driver)

    def check_home_page_title(self,excepted_title_text):
        self.verify_page_title(excepted_title_text)
        # self.driver.title.__eq__(excepted_title_text)

    def search_on_field(self,product_text):
        self.type_into_element("search_field_xpath",self.search_field_xpath,product_text)
        # self.driver.find_element(By.XPATH,self.search_field_xpath).send_keys(product_text)

    def click_on_search_button(self):
        self.click_on_element("click_on_button_xpath",self.click_on_button_xpath)
        # self.driver.find_element(By.XPATH,self.click_on_button_xpath).click()
        return searchpage(self.driver)

    def click_on_register(self):
        self.click_on_element("register_option_xpath",self.register_option_xpath)
        # self.driver.find_element(By.XPATH, self.register_option_xpath).click()
        return registerpage(self.driver)
