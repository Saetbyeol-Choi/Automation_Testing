# # from behave import *
# # from playwright.sync_api import Playwright, sync_playwright, expect, Page
# #
# # playwright = sync_playwright().start()
# #
# # @given('Launch chrome browser')
# # def launchBrowser(context):
# #     context.browser = playwright.chromium.launch(headless=False, slow_mo=3000)
# #
# # # Step definitions for ats.feature
# # @when('Open ATS homepage')
# # def openHomePage(context):
# #     context.page = context.browser.new_page()
# #     context.page.goto("https://automationteststore.com/")
# #
# # @then('Verify that the logo present on page')
# # def verifyLogo(context):
# #     context.page.get_by_role("img", name="Automation Test Store").click()
# #
# # @then('Hover on ACCOUNT button')
# # def hoverOverAccountButton(context):
# #     context.page.get_by_role("link", name="Account").hover()
# #     # context.page.get_by_text("Account").nth(0).hover()
# #     # context.page.locator('a.menu_account').nth(0).hover()
# #
# # @then('Click on LOGIN button')
# # def clickLoginButton(context):
# #     context.page.get_by_role("link", name="Login").nth(0).click()  # nth() method to select the first matching element
# #     # context.page.locator('a.sub.menu_login').nth(0).click()
# #
# # @then('Enter username "{user}" and password "{pwd}"')
# # def enterUserInfo(context, user, pwd):
# #     context.page.locator("#loginFrm_loginname").fill(user)
# #     context.page.locator("#loginFrm_password").fill(pwd)
# #
# # @then('Click on Login button to login')
# # def clickLoginButton_2(context):
# #     context.page.get_by_role("button", name="Login").click()
# #
# # @then('User must successfully see the MY ACCOUNT web page')
# # def checkLoginStatus(context):
# #     # Check if the page contains "My Account" to confirm successful login
# #     if context.page.inner_text("span:has-text('My Account')"):
# #         assert True, "Test Passed: Successfully logged in to MY ACCOUNT."
# #     # Check for error message in case of login failure
# #     elif context.page.inner_text("div.alert-danger:has-text('Error: Incorrect login or password provided.')"):
# #         assert False, "Test Failed: Error: Incorrect login or password provided."
# #     else:
# #         assert False, "Test Failed: Unknown login status."
# #
# #     # if context.page.inner_text("span:has-text('My Account')"):
# #     #     print("Successfully logged in to MY ACCOUNT.")
# #     # elif context.page.inner_text("div.alert-danger:has-text('Error: Incorrect login or password provided.')"):
# #     #     print("Error: Incorrect login or password provided.")
# #     # else:
# #     #     print("Unknown login status")
# #
# # @then('Close browser')
# # def closeBrowser(context):
# #     context.browser.close()
# #
# #
# # # playwright.stop()
# #
# # # @then('click on ACCOUNT button')
# # # def clickAccountButton(context):
# # #     account_element = context.page.locator("link", name="Account")
# # #     login_element = context.page.locator("link", name="Login")
# # #
# # #     # Drag the "Account" element to the "Login" element
# # #     account_element.drag_to(login_element)
# # #
# # # # Optionally, you can also add a step to click on "Login" after the drag-and-drop
# # # @then('click on LOGIN button')
# # # def clickLoginButton(context):
# # #     context.page.locator("link", name="Login").click()
# # # @then('User must successfully see the ACCOUNT LOGIN web page')
# # # def verifyAccountLoginPage(context):
# # #     context.page.wait_for_url('https://automationteststore.com/index.php?rt=account/login')
#
#
# import asyncio
# from playwright.async_api import async_playwright
# from behave import *
#
#
# # Initialize Playwright context with the browser visible
# async def initialize_playwright():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False, slow_mo=6000)  # Set headless to False
#         page = await browser.new_page()
#         return browser, page
#
#
# @given('Launch chrome browser')
# async def launchBrowser(context):
#     loop = asyncio.get_event_loop()
#     context.browser, context.page = loop.run_until_complete(initialize_playwright())
#
#
# @when('Open ATS homepage')
# async def openHomePage(context):
#     await context.page.goto("https://automationteststore.com/")
#
#
# @then('Verify that the logo present on page')
# async def verifyLogo(context):
#     logo = context.page.locator('//header/div[1]/div[1]/div[1]/a[1]/img[1]')
#     assert await logo.is_visible()
#
#
# @then('Hover on ACCOUNT button')
# async def clickAccountButton(context):
#     await context.page.click('text=Account')
#
#
# @then('Click on LOGIN button')
# async def clickLoginButton(context):
#     await context.page.click('text=LOGIN')
#
#
# @then('User must successfully see the ACCOUNT LOGIN web page')
# async def verifyAccountLoginPage(context):
#     await context.page.wait_for_url('https://automationteststore.com/index.php?rt=account/login')
#
#
# # @then('User must successfully see the ACCOUNT LOGIN web page')
# # async def verifyAccountLoginPage(context):
# #     # Wait for the URL to change to the ACCOUNT LOGIN page with a timeout (e.g., 10 seconds)
# #     try:
# #         await context.page.wait_for_url('https://automationteststore.com/index.php?rt=account/login', timeout=10000)
# #     except TimeoutError:
# #         assert False, "Timed out waiting for the ACCOUNT LOGIN page to load"
# #
#
# import asyncio
# from playwright.async_api import async_playwright
#
#
# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False, slow_mo=6000)
#         page = await browser.new_page()
#         await page.goto("https://automationteststore.com/")
#         await browser.close()
#
#
# asyncio.run(main())

import asyncio
from playwright.async_api import async_playwright

from behave import *
import asyncio
from playwright.async_api import async_playwright


# Initialize Playwright outside of an async with to keep it alive
async def initialize_playwright():
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False, slow_mo=6000)
    page = await browser.new_page()
    return p, browser, page


# Store the event loop in the context for reuse
@given('Launch chrome browser')
def launch_browser(context):
    context.loop = asyncio.get_event_loop()
    context.p, context.browser, context.page = context.loop.run_until_complete(initialize_playwright())


@when('Open ATS homepage')
def open_home_page(context):
    context.loop.run_until_complete(context.page.goto("https://automationteststore.com/"))


@then('Verify that the logo present on page')
def verify_logo(context):
    logo = context.page.locator('//header/div[1]/div[1]/div[1]/a[1]/img[1]')
    assert context.loop.run_until_complete(logo.is_visible())

# Continue with the remaining steps similarly...
