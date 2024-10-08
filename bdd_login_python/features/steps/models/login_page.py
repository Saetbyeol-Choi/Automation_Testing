from playwright.sync_api import Page
from Playwright_Test.bdd_login_python.features.steps.models.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.locator("#loginFrm_loginname")
        self.password = page.locator("#loginFrm_password")
        self.submit = page.get_by_role('button', name='login')
        self.reset_password = page.get_by_role('button', name='Forgot Password')

    async def navigate(self):
        await self.page.goto("https://automationteststore.com/", timeout=5000)

    async def fill_username(self, text):
        await self.username.fill(text)

    async def fill_password(self, text):
        await self.password.fill(text)

    async def submit_login(self):
        await self.submit.click()

    async def fill_form_field(self, field, value):
        if field == "username":
            await self.fill_username(value)
        elif field == "password":
            await self.fill_password(value)
        else:
            assert False

    async def click_button(self, action):
        if action == "submit":
            await self.submit_login()
        elif action == "forgot password":
            await self.reset_password.click()
            await self.page.wait_for_timeout(timeout=1000)
        else:
            assert False

    # async def is_error_message_displayed(self):
    #     return await self.page.wait_for_selector(".error-text", state="visible", timeout=5000)
    async def is_error_message_displayed(self):
        return await self.page.locator(".error-text").is_visible()
