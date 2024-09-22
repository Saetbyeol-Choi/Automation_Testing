from behave import *
from selenium import webdriver
# from selenium.webdriver.common.by import By  # Import the 'By' class

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()
    #context.driver=webdriver.Chrome(executable_path=r"C:\Users\sbyeo\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10\chromedriver.exe")

@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://automationteststore.com/")

@then('verify that the logo present on page')
def verifyLogo(context):
    image_element = context.driver.find_element("xpath", "//header/div[1]/div[1]/div[1]/a[1]/img[1]")
    assert image_element.is_displayed()

@then('close browser')
def closeBrowser(context):
    #context.driver.close()
    context.driver.quit()
