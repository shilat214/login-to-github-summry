from playwright.sync_api import Page, expect

from pages.login_github import LoginPage
from utilities.config import TEST_EMAIL_GITHUB, TEST_PASSWORD_GITHUB



def test_sign_in_to_gmail(page: Page):
    signInPage = LoginPage(page)
    signInPage.open()

    expect(signInPage.signInButton).to_be_visible() 

    signInPage.clickOnSignInButton()
    signInPage.emailField.fill(TEST_EMAIL_GITHUB)
    signInPage.passwordField.fill(TEST_PASSWORD_GITHUB)
    signInPage.signInWithCredentials.click()

