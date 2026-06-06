from playwright.sync_api import Page, expect
from data import CREDENTIALS, PRODUCT_DATA, TC05_ORDER_DATA
import pytest


# TC01
def test_tc01_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill(CREDENTIALS["username"])
    page.locator("#password").fill(CREDENTIALS["password"])
    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

# TC02
def test_tc02_add_product_to_the_cart(auth_page):
    for product in PRODUCT_DATA.values():
        add_button = auth_page.locator(product["btn_selectors"]["add_button"])
        remove_button = auth_page.locator(product["btn_selectors"]["remove_button"])

        add_button.click()

        expect(remove_button).to_be_visible()
    
    cart_badge = auth_page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text(str(len(PRODUCT_DATA)))

# TC03
def test_tc03_cart_detail_overview(auth_page_with_cart):
    page = auth_page_with_cart

    cart_button = page.locator(".shopping_cart_link")
    cart_button.click()

    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    for product in PRODUCT_DATA.values():
        cart_item = page.locator(".cart_item").filter(has_text=product["product_name"])

        expect(cart_item.locator(".cart_quantity")).to_have_text("1")
        expect(cart_item.locator(".inventory_item_name")).to_have_text(product["product_name"])
        expect(cart_item.locator(".inventory_item_price")).to_have_text(f"${product['price']}")
        expect(cart_item.locator(product["btn_selectors"]["remove_button"])).to_be_visible()

    checkout_button = page.locator("#checkout")
    expect(checkout_button).to_be_visible()

# TC04
@pytest.mark.parametrize("first_name, last_name, zip_code, error_message", [
    ("", "", "", "Error: First Name is required"),
    ("John", "", "", "Error: Last Name is required"),
    ("John", "Doe", "", "Error: Postal Code is required")
], ids=["TC04-1", "TC04-2", "TC04-3"])
def test_tc04_submit_invalid_order(auth_page_with_cart, first_name, last_name, zip_code, error_message):
    page = auth_page_with_cart

    page.goto("https://www.saucedemo.com/checkout-step-one.html")

    page.locator("#first-name").fill(first_name)
    page.locator("#last-name").fill(last_name)
    page.locator("#postal-code").fill(zip_code)
    page.locator("#continue").click()

    error_handler = page.locator(".error-message-container")

    expect(error_handler).to_be_visible()
    expect(error_handler).to_have_text(error_message)


# TC05
def test_tc_05_submit_order(auth_page_with_cart):
    page = auth_page_with_cart
    
    page.goto("https://www.saucedemo.com/checkout-step-one.html")

    page.locator("#first-name").fill(TC05_ORDER_DATA["first_name"])
    page.locator("#last-name").fill(TC05_ORDER_DATA["last_name"])
    page.locator("#postal-code").fill(TC05_ORDER_DATA["zip_code"])
    page.locator("#continue").click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    summary = page.locator(".summary_total_label")
    expect(summary).to_have_text("Total: $43.18")

    finish_btn = page.locator("#finish")
    expect(finish_btn).to_be_visible()
    expect(finish_btn).to_have_text("Finish")
    finish_btn.click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    title = page.locator("#checkout_complete_container > h2")
    expect(title).to_have_text("Thank you for your order!")


# TC06
def test_tc_06logout(auth_page):
    menu_btn = auth_page.locator("#react-burger-menu-btn")
    menu_btn.click()

    expect(menu_btn).to_be_visible()

    logout_btn = auth_page.locator("#logout_sidebar_link")
    logout_btn.click()

    expect(auth_page).not_to_have_url("https://www.saucedemo.com/inventory.html")
    expect(auth_page).to_have_url("https://www.saucedemo.com/")


    #Overenie či je user skutočne odhlásený
    auth_page.goto("https://www.saucedemo.com/inventory.html")

    expect(auth_page).to_have_url("https://www.saucedemo.com/")
    error_box = auth_page.locator(".error-message-container.error")
    error_text = auth_page.locator(".error-message-container.error > h3")

    expect(error_box).to_be_visible()
    expect(error_text).to_have_text("Epic sadface: You can only access '/inventory.html' when you are logged in.")

    




