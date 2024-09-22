from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://automationteststore.com/index.php?rt=account/login")

@then('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    # context.driver.find_element_by_id("loginFrm_loginname").send_keys(user)
    # context.driver.find_element_by_id("loginFrm_password").send_keys(pwd)
    # context.driver.find_element_by_name("username").send_keys(user)
    # context.driver.find_element_by_name("password").send_keys(pwd)

    user_input = context.driver.find_element(By.ID, "loginFrm_loginname")
    pwd_input = context.driver.find_element(By.ID, "loginFrm_password")

    user_input.send_keys(user)
    pwd_input.send_keys(pwd)

@then('Click on login button')
def step_impl(context):
    # context.driver.find_element_by_id("Login").click()
    # context.driver.find_element_by_name("Login").click()
    login_button = context.driver.find_element(By.CSS_SELECTOR, 'button[title="Login"]')
    login_button.click()

# #Scenario
# @then('User must successfully login to the My Account page')
# def step_impl(context):
#     #text = context.driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[8]/a[1]/span[1]").text()
#     # text = context.driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[8]/a[1]/span[1]").text
#     my_account_link = context.driver.find_element(By.XPATH,
#                                                   "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'my account')]")
#     assert my_account_link.text == "My Account"
#     context.driver.close()

#Scenario Ouline
@then('User must successfully login to the My Account page')
def step_impl(context):
    try:
        #text = context.driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[8]/a[1]/span[1]").text()
        # text = context.driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[8]/a[1]/span[1]").text
        text = context.driver.find_element_by_name("MY ACCOUNT").nth(0)
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "My Account":
        context.driver.close()
        assert True, "Test Passed"
