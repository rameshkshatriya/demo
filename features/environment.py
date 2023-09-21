import time

from selenium import webdriver
from utilities import configReader


def before_scenario(context, driver):
    browser_name = configReader.read_configuration("basic info", "browser")

    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    time.sleep(10)
    context.driver.get(configReader.read_configuration("basic info", "url"))


def after_scenario(context, driver):
    time.sleep(10)
    context.driver.quit()