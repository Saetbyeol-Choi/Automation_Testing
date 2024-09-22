from behave import *
from playwright.sync_api import Playwright, sync_playwright, expect, Page
import parse

playwright = sync_playwright().start()

@parse.with_pattern(r".*")  # zero or more occurances of any character
def parse_string(text):
    return text.strip()

register_type(Val=parse_string)

@given('Launch chrome browser')
def launchBrowser(context):
    context.browser = playwright.chromium.launch(headless=False) #, slow_mo=3000)

@when('Open ATS homepage')
def openHomePage(context):
    context.page = context.browser.new_page()
    context.page.goto("https://automationteststore.com/")

@then('Click ACCOUNT button')
def hoverOverAccountButton(context):
    context.page.get_by_role("link", name="Account").hover()
    # context.page.get_by_role("link", name="Account").click()
    # context.page.locator("span").filter(has_text="Account")

@then('Select Login')
def selectLogin(context):
    context.page.get_by_role("link", name="Login").nth(0).click()

@then('Click on Continue button')
def clickContinueButton(context):
    context.page.get_by_role("button", name="Continue").click()

@then('Enter Personal Details "{firstname:Val}", "{lastname:Val}", "{email:Val}"')
def enterUserInfo(context, firstname, lastname, email):
    context.page.locator("#AccountFrm_firstname").fill(firstname)
    context.page.locator("#AccountFrm_lastname").fill(lastname)
    context.page.locator("#AccountFrm_email").fill(email)

# @then('Enter Personal Details "{firstname}", "{lastname}", "{email}"')
# def enterUserInfo(context, firstname, lastname, email):
#     if firstname == '""':
#         firstname = ""
#     elif lastname == '""':
#         lastname = ""
#     elif email == '"':
#         email = ""
#     context.page.locator("#AccountFrm_firstname").fill(firstname)
#     context.page.locator("#AccountFrm_lastname").fill(lastname)
#     context.page.locator("#AccountFrm_email").fill(email)

@then('Enter Address "{address1:Val}", "{city:Val}", "{state:Val}", "{zipcode:Val}", "{country:Val}"')
def enterAddress(context, address1, city, state, zipcode, country):
    context.page.locator("#AccountFrm_address_1").fill(address1)
    context.page.locator("#AccountFrm_city").fill(city)
    context.page.locator("#AccountFrm_country_id").select_option(label = country)
    context.page.locator("#AccountFrm_postcode").fill(zipcode)
    context.page.locator("#AccountFrm_zone_id").select_option(label = state)

# @then('Enter Address "{address1}", "{city}", "{state}", "{zipcode}", "{country}"')
# def enterAddress(context, address1, city, state, zipcode, country):
#     if address1 == '""':
#         address1 = ""
#     elif city == '""':
#         city = ""
#     elif state == '""':
#         state = ""
#     context.page.locator("#AccountFrm_address_1").fill(address1)
#     context.page.locator("#AccountFrm_city").fill(city)
#     context.page.locator("#AccountFrm_country_id").select_option(label = country)
#     context.page.locator("#AccountFrm_postcode").fill(zipcode)
#     context.page.locator("#AccountFrm_zone_id").select_option(label = state)

@then('Enter Login Details "{loginname:Val}", "{password:Val}", "{pwdconfirm:Val}"')
def enterLoginDetails(context, loginname, password, pwdconfirm):
    context.page.locator("#AccountFrm_loginname").fill(loginname)
    context.page.locator("#AccountFrm_password").fill(password)
    context.page.locator("#AccountFrm_confirm").fill(pwdconfirm)

@then('Check on policy')
def checkbox(context):
    context.page.locator("#AccountFrm_agree").check()

@then('Submit the registration form')
def submitForm(context):
    context.page.get_by_role("button", name="Continue").click()




@then('Verify successful registration')
def verifyRegistration(context):
    context.page.wait_for_selector("span.maintext i.fa-thumbs-up", timeout=5000)
    success_message = context.page.locator("span.maintext i.fa-thumbs-up").text()
    assert "Your Account Has Been Created!" == success_message, f"Expected success message not found. Actual message: {success_message}"


@then('Verify registration error message')
def verifyErrorMessage(context):
    context.page.wait_for_selector(".alert.alert-error.alert-danger")
    error_message = context.page.locator(".alert.alert-error.alert-danger").inner_text()
    print(error_message)
    expected_error = "Error: You must agree to the Privacy Policy!"
    assert expected_error == error_message, f"Expected error message not found. Actual message: {error_message}"



@then('Verify missing first name error message')
def verifyMissingFirstNameError(context):
    context.page.wait_for_selector("span.help-block:has-text('First Name must be between 1 and 32 characters!')")
    error_message = context.page.locator("span.help-block:has-text('First Name must be between 1 and 32 characters!')").inner_text()
    assert "First Name must be between 1 and 32 characters!" == error_message, True

@then('Verify missing last name error message')
def verifyMissingLastNameError(context):
    context.page.wait_for_selector("span.help-block:has-text('Last Name must be between 1 and 32 characters!')")
    error_message = context.page.locator("span.help-block:has-text('Last Name must be between 1 and 32 characters!')").inner_text()
    assert "Last Name must be between 1 and 32 characters!" == error_message, True

@then('Verify invalid email error message')
def verifyInvalidEmailError(context):
    context.page.wait_for_selector("span.help-block:has-text('Email Address does not appear to be valid!')")
    error_message = context.page.locator("span.help-block:has-text('Email Address does not appear to be valid!')").inner_text()
    assert "Email Address does not appear to be valid!" == error_message, True

@then('Verify missing address 1 error message')
def verifyMissingAddress1Error(context):
    context.page.wait_for_selector("span.help-block:has-text('Address 1 must be between 3 and 128 characters!')")
    error_message = context.page.locator("span.help-block:has-text('Address 1 must be between 3 and 128 characters!')").inner_text()
    assert "Address 1 must be between 3 and 128 characters!" in error_message, True

@then('Verify missing city error message')
def verifyMissingCityError(context):
    context.page.wait_for_selector("span.help-block:has-text('City must be between 3 and 128 characters!')")
    error_message = context.page.locator("span.help-block:has-text('City must be between 3 and 128 characters!')").inner_text()
    assert "City must be between 3 and 128 characters!" in error_message, True

@then('Verify missing state error message')
def verifyMissingStateError(context):
    context.page.wait_for_selector("span.help-block:has-text('Please select a region / state!')")
    error_message = context.page.locator("span.help-block:has-text('Please select a region / state!')").inner_text()
    assert "Please select a region / state!" in error_message, True

@then('Close the browser')
def closeBrowser(context):
    context.browser.close()


# @then('Verify registration error message_check box')
# def verifyErrorMessage(context):
#     context.page.wait_for_selector(".alert-error")  # Wait for error message
#     error_message = context.page.locator(".alert-error").inner_text()
#     assert "You must agree to the Privacy Policy!" in error_message, "Privacy Policy error message not found."
