from selenium.webdriver.common.by import By

from features.pages.accountsuccesspage import accountsuccesspage
from features.pages.basepage import basepage


class registerpage(basepage):

    def __init__(self,driver):
        super().__init__(driver)

    first_name_field_xpath = "//div/input[@name='firstname']"
    last_name_field_xpath = "//div/input[@name='lastname']"
    new_email_field_xpath = "//div/input[@name='email']"
    telephone_field_xpath = "//div/input[@name='telephone']"
    password_field_xpath = "//div/input[@name='password']"
    conform_password_field_xpath = "//div/input[@name='confirm']"
    select_private_policy_xpath = "//input[@name='agree']"
    click_on_continue_button_xpath = "//input[@value='Continue']"
    newsletter_subsribe_xpath = "//div/label[1]/input[@name='newsletter'][@value='1']"
    duplicate_email_warning_xpath = "//div[@id='account-register']/div[1]"
    invalid_email_xpath = "//div/input[@name='email']"
    excepted_private_policy_warning_xpath = "//div[@id = 'account-register']/div[1]"
    excepted_firstname_warning_xpath = "//div/input[@id = 'input-firstname']/following-sibling::div"
    excepted_lastname_warning_xpath = "//div/input[@id = 'input-lastname']/following-sibling::div"
    excepted_email_warning_xpath = "//div/input[@id = 'input-email']/following-sibling::div"
    excepted_telephone_warning_xpath = "//div/input[@id = 'input-telephone']/following-sibling::div"
    expected_password_warning_xpath = "//div/input[@id = 'input-password']/following-sibling::div"


    def send_first_name_to_field(self,first_name):
        self.type_into_element("first_name_field_xpath",self.first_name_field_xpath,first_name)
        # self.driver.find_element(By.XPATH, self.first_name_field_xpath).send_keys(first_name)

    def send_last_name_to_field(self,last_name):
        self.type_into_element("last_name_field_xpath",self.last_name_field_xpath,last_name)
        # self.driver.find_element(By.XPATH, self.last_name_field_xpath).send_keys(last_name)

    def send_new_email_to_field(self,email_text):
        self.type_into_element("new_email_field_xpath",self.new_email_field_xpath,email_text)
        # self.driver.find_element(By.XPATH, self.new_email_field_xpath).send_keys(email_text)

    def send_telephone_num_to_field(self,telephone_text):
        self.type_into_element("telephone_field_xpath",self.telephone_field_xpath,telephone_text)
        # self.driver.find_element(By.XPATH , self.telephone_field_xpath).send_keys(telephone_text)

    def send_password_to_field(self,password_text):
        self.type_into_element("password_field_xpath",self.password_field_xpath,password_text)
        # self.driver.find_element(By.XPATH ,self.password_field_xpath).send_keys(password_text)

    def send_conform_password_to_field(self,conform_passwd_text):
        self.type_into_element("conform_password_field_xpath",self.conform_password_field_xpath,conform_passwd_text)
        # self.driver.find_element(By.XPATH ,self.conform_password_field_xpath).send_keys(conform_passwd_text)

    def select_private_policy_button(self):
        self.click_on_element("select_private_policy_xpath",self.select_private_policy_xpath)
        # self.driver.find_element(By.XPATH ,self.select_private_policy_xpath).click()

    def click_on_continue_button(self):
        self.click_on_element("click_on_continue_button_xpath",self.click_on_continue_button_xpath)
        # self.driver.find_element(By.XPATH , self.click_on_continue_button_xpath).click()
        return accountsuccesspage(self.driver)

    def newsletter_button(self):
        self.click_on_element("newsletter_subsribe_xpath",self.newsletter_subsribe_xpath)
        # self.driver.find_element(By.XPATH, self.newsletter_subsribe_xpath).click()

    def invaild_email(self,invalid_text):
        self.type_into_element("invalid_email_xpath",self.invalid_email_xpath,invalid_text)
        # self.driver.find_element(By.XPATH, self.invalid_email_xpath).send_keys(invalid_text)

    def duplicate_email_warning(self,duplicate_warning_text):
        self.reterive_element_text_contains("duplicate_email_warning_xpath",self.duplicate_email_warning_xpath,duplicate_warning_text)
        # assert self.driver.find_element(By.XPATH, self.duplicate_email_warning_xpath).text.__contains__(duplicate_warning_text)

    def display_status_of_all_warnings(self,expected_private_policy_text,firstname_warning_text,lastname_warning_text,email_warning_text,telephone_warning_text,password_warning_text):
        privacy_status = self.reterive_element_text_equals("excepted_private_policy_warning_xpath", self.excepted_private_policy_warning_xpath ,expected_private_policy_text)
        firstname_status = self.reterive_element_text_equals("excepted_firstname_warning_xpath", self.excepted_firstname_warning_xpath,firstname_warning_text)
        lastname_status = self.reterive_element_text_equals("excepted_lastname_warning_xpath", self.excepted_lastname_warning_xpath,lastname_warning_text)
        email_status = self.reterive_element_text_equals("excepted_email_warning_xpath", self.excepted_email_warning_xpath,email_warning_text)
        telephone_status = self.reterive_element_text_equals("excepted_telephone_warning_xpath", self.excepted_telephone_warning_xpath,telephone_warning_text)
        password_status = self.reterive_element_text_equals("expected_password_warning_xpath", self.expected_password_warning_xpath,password_warning_text)
        return self.status_result(privacy_status,firstname_status,lastname_status,email_status,telephone_status,password_status)
        # privacy_status = self.driver.find_element(By.XPATH, self.excepted_private_policy_warning_xpath).text.__eq__(expected_private_policy_text)
        # firstname_status = self.driver.find_element(By.XPATH, self.excepted_firstname_warning_xpath).text.__eq__(firstname_warning_text)
        # lastname_status = self.driver.find_element(By.XPATH, self.excepted_lastname_warning_xpath).text.__eq__(lastname_warning_text)
        # email_status = self.driver.find_element(By.XPATH, self.excepted_email_warning_xpath).text.__eq__(email_warning_text)
        # telephone_status = self.driver.find_element(By.XPATH, self.excepted_telephone_warning_xpath).text.__eq__(telephone_warning_text)
        # password_status = self.driver.find_element(By.XPATH, self.expected_password_warning_xpath).text.__eq__(password_warning_text)
        # if privacy_status and firstname_status and lastname_status and email_status and telephone_status and password_status:
        #     return True
        # else:
        #     return False
