from behave import *
from playwright.sync_api import Playwright, sync_playwright, expect, Page

playwright = sync_playwright().start()

@given('Launch chrome browser')
def launchBrowser(context):
    context.browser = playwright.chromium.launch(headless=False, slow_mo=3000)

# Step definitions for ats.feature
@when('Open ATS homepage')
def openHomePage(context):
    context.page = context.browser.new_page()
    context.page.goto("https://automationteststore.com/")

@then('Click ACCOUNT button')
def hoverOverAccountButton(context):
    # context.page.get_by_role("link", name="Account").hover()
    # context.page.get_by_role("link", name="Account").click()
    context.page.get_by_role("link", name="Account").click()

@then('Select Login')
def selectLogin(context):
    context.page.get_by_role("link", name="Login").nth(0).click()

@then('Click on Continue botton')
def clickContinueButton(context):
    context.page.get_by_role("button", name="Continue").click()

@then('Enter Personal Details "{firstname}", "{lastname}", "{email}"')
def enterUserInfo(context, firstname, lastname, email):
    context.page.locator("#AccountFrm_firstname").fill(firstname)
    context.page.locator("#AccountFrm_lastname").fill(lastname)
    context.page.locator("#AccountFrm_email").fill(email)

@then('Enter Address "{address1}", "{city}", "{state}", "{zipcode}", "{country}"')
def enterAddress(context, address1, city, state, zipcode, country):
    context.page.locator("#AccountFrm_address_1").fill(address1)
    context.page.locator("#AccountFrm_city").fill(city)
    context.page.locator("#AccountFrm_country_id").select_option(label = country)
    context.page.locator("#AccountFrm_postcode").fill(zipcode)
    context.page.locator("#AccountFrm_zone_id").select_option(label = state)

@then('Enter Login Details "{loginname}", "{password}", "{pwdconfirm}"')
def enterLoginDetails(context, loginname, password, pwdconfirm):
    context.page.locator("#AccountFrm_loginname").fill(loginname)
    context.page.locator("#AccountFrm_password").fill(password)
    context.page.locator("#AccountFrm_confirm").fill(pwdconfirm)

@when('Submit the registration form')
def submitRegistrationForm(context):
    context.page.get_by_role("button", name="Continue").click()

@then('Verify successful registration')
def verifySuccessfulRegistration(context):
    assert context.page.inner_text("span:has-text('My Account')"), "Registration failed."

@then('Verify email validation error')
def verifyEmailValidationError(context):
    error_message = context.page.locator(".text-danger").first()
    assert "Email Address does not appear to be valid!" in error_message.inner_text(), "Email validation error not displayed."

# ... Your existing code ...





# @then('Click Main Menu')
# def clickMainMenu(context):
#     context.page.locator("span").filter(has_text="Main Menu")

# @then('Select Login')
# def selectLogin(context):
#     context.page.locator("#main_menu a").filter(has_text="Account").click()




# @then('Click on Login button to login')
# def clickLoginButton_2(context):
#     context.page.get_by_role("button", name="Login").click()
#
# @then('User must successfully see the MY ACCOUNT web page')
# def verifySuccessfulLogin(context):
#     # print(context.page.inner_text("body"))  # Print the inner text of the whole page
#
#     # Check if the page contains "My Account" to confirm successful login
#     if context.page.inner_text("span:has-text('My Account')"):
#         assert True, "Test Passed: Successfully logged in to MY ACCOUNT."
#     else:
#         assert False, "Test Failed: Unknown login status."
#
# @then('Close browser')
# def closeBrowser(context):
#     context.browser.close()