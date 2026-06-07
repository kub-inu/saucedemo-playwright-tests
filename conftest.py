from playwright.sync_api import Page, expect
from src.test_data import CREDENTIALS, PRODUCT_DATA
import pytest

@pytest.fixture
def auth_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    page.locator("#user-name").fill(CREDENTIALS["username"])
    page.locator("#password").fill(CREDENTIALS["password"])
    page.locator("#login-button").click()

    return page

@pytest.fixture
def auth_page_with_cart(auth_page):
    for product in PRODUCT_DATA.values():
        add_button = auth_page.locator(product["btn_selectors"]["add_button"])
        remove_button = auth_page.locator(product["btn_selectors"]["remove_button"])

        add_button.click()

        expect(remove_button).to_be_visible()
    
    return auth_page