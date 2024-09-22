from behave import given, when, then
from behave.api.async_step import async_run_until_complete

# from bdd_login_python.models import login_page, base_page, account_page
from Playwright_Test.bdd_login_python.features.steps.models.account_page import AccountPage
from Playwright_Test.bdd_login_python.features.steps.models.base_page import BasePage
from Playwright_Test.bdd_login_python.features.steps.models.login_page import LoginPage


# use_step_matcher("re")

@given('the login page is open')
@async_run_until_complete
async def open_login_url(context):
    login_page = LoginPage(context.page)
    await login_page.navigate()


@when('i fill "{field}" on Login page with value "{value}"')
@async_run_until_complete
async def fill_login_page_field(context, field: str, value: str):
    """
    :param context: behave.runner.Context
    :param field:
    :type value:
    """
    login_page = LoginPage(context.page)
    await login_page.fill_form_field(field, value)


@when('i click "submit" button on the login page')
@async_run_until_complete
async def click_login_page_button(context, action: str):
    """
    :type context: behave.runner.Context
    :param action:
    """
    login_page = LoginPage(context.page)
    await login_page.click_button(action)


@then('the next page is "{title}" page')
@async_run_until_complete
async def is_next_page(context, title: str):
    """
    :type context: behave.runner.Context
    :param title:
    """
    base_page = LoginPage(context.page)
    assert await base_page.is_title_contains(title)


@then('the error message on login page is visible')
@async_run_until_complete
async def is_login_error_message(context):
    """
    :type context: behave.runner.Context
    """
    login_page = BasePage(context.page)
    await login_page.is_error_message_displayed()


@then('the welcome text on Account page contains the value "{user}"')
@async_run_until_complete
async def step_impl(context, user: str):
    """
    :type context: behave.runner.Context
    :param user:
    """
    account_page = AccountPage(context.page)
    assert await account_page.is_welcome_text_contains(user)
