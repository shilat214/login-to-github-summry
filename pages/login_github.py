from playwright.sync_api import Locator, Page


from pages.base_page import BasePage
from utilities import config
import re


class LoginPage(BasePage):
    PATH = config.GITHUB_URL


    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def signInButton(self) -> Locator:
        return self.page.get_by_role("link", name="Sign in")

    def clickOnSignInButton(self):
     self.page.get_by_role("link", name="Sign in").click()
     self.page.wait_for_url("**/login")

    @property
    def emailField(self) -> Locator:
        return self.page.get_by_role("textbox", name="Username or email address")

    @property   
    def passwordField(self) -> Locator:
            return self.page.get_by_role("textbox", name="Password")
    @property
    def signInWithCredentials(self) -> Locator:
            return self.page.get_by_role("button", name="Sign in", exact=True)