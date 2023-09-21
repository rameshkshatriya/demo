from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.homepage import homepage
from features.pages.searchpage import searchpage


@given(u'I got navigated to home page')
def step_impl(context):
    context.homepage = homepage(context.driver)
    context.homepage.check_home_page_title("Your Store")


@when(u'I enter valid product say "{product}" into the search box field')
def step_impl(context,product):
    # context.homepage = homepage(context.driver)
    context.homepage.search_on_field(product)


@when(u'I click on search button')
def step_impl(context):
    context.searchpage = context.homepage.click_on_search_button()


@then(u'Valid product should get displayed in search results')
def step_impl(context):
    context.searchpage.display_status_of_product()



@when(u'I entered invalid product say "{product}" into the search box field')
def step_impl(context,product):
    # context.homepage = searchpage(context.driver)
    context.homepage.search_on_field(product)


@then(u'Proper message should be displayed in search results')
def step_impl(context):
    # expected_text = "There is no product that matches the search criteria."
    context.searchpage.invalid_product_warning_message("There is no product that matches the search criteria.")



@when(u'I dont enter anything into search box field')
def step_impl(context):
    context.homepage.search_on_field("")

