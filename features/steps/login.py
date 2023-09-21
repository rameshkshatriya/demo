from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.accountpage import accountpage
from features.pages.homepage import homepage
from features.pages.loginpage import loginpage
from utilities import emailwithtimestampgenerator


@given(u'I navigated to login page')
def step_impl(context):
    context.home_page = homepage(context.driver)
    context.home_page.click_on_my_account()
    context.login_page = context.home_page.click_on_login()


@when(u'I enter valid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.send_email_text(email)
    context.login_page.send_password_text(password)


@when(u'I click on login button')
def step_impl(context):
    context.account_page = context.login_page.click_login_button()


@then(u'I should get logged in')
def step_impl(context):
    context.account_page.edit_account_information()


@when(u'I enter invalid email and valid password say "{password}" into the fields')
def step_impl(context, password):
    invalid_email = emailwithtimestampgenerator.get_new_email_with_timestamp()
    context.login_page.send_email_text(invalid_email)
    context.login_page.send_password_text(password)


@then(u'I should get a proper warning message')
def step_impl(context):
    # warning_message = "Warning: No match for E-Mail Address and/or Password."
    context.login_page.proper_warning_message("Warning: No match for E-Mail Address and/or Password.")


@when(u'I entered valid email say "{email}" and invalid password say "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.send_email_text(email)
    context.login_page.send_password_text(password)


@when(u'I enter invalid email and invalid password say "{password}" into the fields')
def step_impl(context, password):
    invalid_email = emailwithtimestampgenerator.get_new_email_with_timestamp()
    context.login_page.send_email_text(invalid_email)
    context.login_page.send_password_text(password)


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    context.login_page.send_email_text("")
    context.login_page.send_password_text("")
