from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.accountsuccesspage import accountsuccesspage
from features.pages.homepage import homepage
from features.pages.registerpage import registerpage
from utilities import emailwithtimestampgenerator


@given(u'I navigate to register page')
def step_impl(context):
    context.homepage = homepage(context.driver)
    context.homepage.click_on_my_account()
    context.register_page = context.homepage.click_on_register()


@when(u'I entered below details into all mandatory felds')
def step_impl(context):
    for row in context.table:
        context.register_page.send_first_name_to_field(row["first_name"])
        context.register_page.send_last_name_to_field(row["last_name"])
        new_mail = emailwithtimestampgenerator.get_new_email_with_timestamp()
        context.register_page.send_new_email_to_field(new_mail)
        context.register_page.send_telephone_num_to_field(row["telephone"])
        context.register_page.send_password_to_field(row["password"])
        context.register_page.send_conform_password_to_field(row["password"])

@when(u'select the private policy')
def step_impl(context):
    context.register_page.select_private_policy_button()

@when(u'I click on continue button')
def step_impl(context):
    context.account_successpage = context.register_page.click_on_continue_button()


@then(u'Account should get created')
def step_impl(context):
    context.account_successpage.register_account_success("Your Account Has Been Created!")


@when(u'I entered below details into all fields')
def step_impl(context):
    for row in context.table:
        context.register_page.send_first_name_to_field(row["first_name"])
        context.register_page.send_last_name_to_field(row["last_name"])
        new_mail = emailwithtimestampgenerator.get_new_email_with_timestamp()
        context.register_page.send_new_email_to_field(new_mail)
        context.register_page.send_telephone_num_to_field(row["telephone"])
        context.register_page.send_password_to_field(row["password"])
        context.register_page.send_conform_password_to_field(row["password"])
        context.register_page.newsletter_button()


@when(u'I entered below details into all fields except email field')
def step_impl(context):
    for row in context.table:
        context.register_page.send_first_name_to_field(row["first_name"])
        context.register_page.send_last_name_to_field(row["last_name"])
        context.register_page.send_telephone_num_to_field(row["telephone"])
        context.register_page.send_password_to_field(row["password"])
        context.register_page.send_conform_password_to_field(row["password"])
        context.register_page.newsletter_button()



@when(u'I entered existing accounts email into email filed')
def step_impl(context):
    context.register_page.invaild_email("rakesh1234@gmail.com")
    # context.driver.find_element(By.XPATH, "//div/input[@name='email']").send_keys("rakesh1234@gmail.com")


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    # expected_error = "Warning: E-Mail Address is already registered!"
    context.register_page.duplicate_email_warning("Warning: E-Mail Address is already registered!")



@when(u'I dont enter anything into the fields')
def step_impl(context):
    # context.driver.find_element(By.XPATH, "//div/input[@name='firstname']").send_keys("")
    # context.driver.find_element(By.XPATH, "//div/input[@name='lastname']").send_keys("")
    # context.driver.find_element(By.XPATH, "//div/input[@name='telephone']").send_keys("")
    # context.driver.find_element(By.XPATH, "//div/input[@name='password']").send_keys("")
    # context.driver.find_element(By.XPATH, "//div/input[@name='confirm']").send_keys("")
    context.register_page.send_first_name_to_field("")
    context.register_page.send_last_name_to_field("")
    context.register_page.send_telephone_num_to_field("")
    context.register_page.send_password_to_field("")
    context.register_page.send_conform_password_to_field("")




@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    excepted_private_policy_warning = "Warning: You must agree to the Privacy Policy!"
    excepted_firstname_warning = "First Name must be between 1 and 32 characters!"
    excepted_lastname_warning = "Last Name must be between 1 and 32 characters!"
    excepted_email_warning = "E-Mail Address does not appear to be valid!"
    excepted_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"
    context.register_page.display_status_of_all_warnings(excepted_private_policy_warning,excepted_firstname_warning,excepted_lastname_warning,excepted_email_warning,excepted_telephone_warning,expected_password_warning)
    # assert context.driver.find_element(By.XPATH,"//div[@id = 'account-register']/div[1]").text.__contains__(excepted_private_policy_warning)
    # assert context.driver.find_element(By.XPATH,"//div/input[@id = 'input-firstname']/following-sibling::div").text.__contains__(excepted_firstname_warning)
    # assert context.driver.find_element(By.XPATH,"//div/input[@id = 'input-lastname']/following-sibling::div").text.__contains__(excepted_lastname_warning)
    # assert context.driver.find_element(By.XPATH,"//div/input[@id = 'input-email']/following-sibling::div").text.__contains__(excepted_email_warning)
    # assert context.driver.find_element(By.XPATH,"//div/input[@id = 'input-telephone']/following-sibling::div").text.__contains__(excepted_telephone_warning)
    # assert context.driver.find_element(By.XPATH,"//div/input[@id = 'input-password']/following-sibling::div").text.__contains__(expected_password_warning)


