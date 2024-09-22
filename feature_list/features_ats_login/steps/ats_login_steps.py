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

@then('Verify that the logo present on page')
def verifyLogo(context):
    context.page.get_by_role("img", name="Automation Test Store").click()

@then('Hover on ACCOUNT button')
def hoverOverAccountButton(context):
    context.page.get_by_role("link", name="Account").hover()
    # context.page.get_by_text("Account").nth(0).hover()
    # context.page.locator('a.menu_account').nth(0).hover()

@then('Click on LOGIN button')
def clickLoginButton(context):
    context.page.get_by_role("link", name="Login").nth(0).click()  # nth() method to select the first matching element
    # context.page.locator('a.sub.menu_login').nth(0).click()

@then('Enter username "{user}" and password "{pwd}"')
def enterUserInfo(context, user, pwd):
    context.page.locator("#loginFrm_loginname").fill(user)
    context.page.locator("#loginFrm_password").fill(pwd)

@then('Click on Login button to login')
def clickLoginButton_2(context):
    context.page.get_by_role("button", name="Login").click()

@then('User must successfully see the MY ACCOUNT web page')
def verifySuccessfulLogin(context):
    # print(context.page.inner_text("body"))  # Print the inner text of the whole page

    # Check if the page contains "My Account" to confirm successful login
    if context.page.inner_text("span:has-text('My Account')"):
        assert True, "Test Passed: Successfully logged in to MY ACCOUNT."
    else:
        assert False, "Test Failed: Unknown login status."

@then('Close browser')
def closeBrowser(context):
    context.browser.close()


# from playwright.async_api import async_playwright, Playwright
# async def before_all(context):
#     context.playwright = await async_playwright().start()
#
# async def after_all(context):
#     await context.playwright.stop()
#
# @given('Launch chrome browser')
# async def launchBrowser(context):
#     context.browser = await playwright.chromium.launch(headless=False, slow_mo=3000)
#
# # Step definitions for ats_login.feature
# @when('Open ATS homepage')
# async def openHomePage(context):
#     context.page = await context.browser.new_page()
#     await context.page.goto("https://automationteststore.com/")
#
# @then('Verify that the logo is present on the page')
# async def verifyLogo(context):
#     await context.page.locator("img", name="Automation Test Store").click()
#
# @then('Hover on ACCOUNT button')
# async def hoverOverAccountButton(context):
#     await context.page.locator("link", name="Account").nth(0).click()
#
# @then('Click on LOGIN button')
# async def clickLoginButton(context):
#     await context.page.locator("link", name="Login").nth(0).click()
#
# @then('Enter username "{user}" and password "{pwd}"')
# async def enterUserInfo(context, user, pwd):
#     await context.page.locator("#loginFrm_loginname").fill(user)
#     await context.page.locator("#loginFrm_password").fill(pwd)
#
# @then('Click on Login button to login')
# async def clickLoginButton_2(context):
#     await context.page.locator("button", name="Login").click()
