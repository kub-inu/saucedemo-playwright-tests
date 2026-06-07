from playwright.sync_api import Page, expect
from help_functions import summary_price
from test_data import CREDENTIALS, PRODUCT_DATA, TC05_ORDER_DATA, TAX_RATE
import pytest

def test_tc01_login_user_with_valid_credentials(page: Page) -> None:
    """  
    TC01: Ověření úspěšného přihlášení uživatele do e-shopu. 
    Detail na testovací případ: ../docs/testovaci-pripady.md
    """

    page.goto("https://www.saucedemo.com/")
    
    # Vyplnení přihlasovacího formuláře
    page.locator("#user-name").fill(CREDENTIALS["username"])
    page.locator("#password").fill(CREDENTIALS["password"])
    page.locator("#login-button").click()

    # Ověření, že je uživatel přesměrován na stránku '/inventory.html'
    expect(
        page, 
        f"Očekávaným výsledkem je přesměrování na '/inventory.html', ale uživatel je přesměrován na: {page.url}"
        ).to_have_url("https://www.saucedemo.com/inventory.html")
    
    product_list = page.locator("#inventory_container > .inventory_list > .inventory_item").all()
    expect(
        product_list[0], 
        "Na stránce má být zobrazen alespoň jeden produkt e-shopu."
        ).to_be_visible()
    

def test_tc02_add_product_to_the_cart(auth_page: Page) -> None:
    """ 
    TC02: Přidání produktu do nákupního košíku 
    Detail na testovací případ: ../docs/testovaci-pripady.md
    """

    cart_badge = auth_page.locator(".shopping_cart_badge")

    # Kliknutí na 'Add to cart' a ověření, že se tlačitko změní na 'Remove'
    # Iretace skrze předpripravené testovací data PRODUCT_DATA
    for product in PRODUCT_DATA.values():
        # Arrange
        add_button = auth_page.locator(product["btn_selectors"]["add_button"])
        remove_button = auth_page.locator(product["btn_selectors"]["remove_button"])

        # Act
        add_button.click()

        #Assert
        expect(remove_button).to_be_visible()
    
    # ASSERT
    expect(cart_badge).to_have_text(str(len(PRODUCT_DATA)))


def test_tc03_cart_detail_overview(auth_page_with_cart: Page) -> None:
    """ 
    TC03: Ověření detailu nákupního košíku.
    Detail na testovací případ: ../docs/testovaci-pripady.md
    """

    page = auth_page_with_cart

    # Kliknutí na ikonu nákupního košíku na stránce '/inventory.html'
    cart_button = page.locator(".shopping_cart_link")
    cart_button.click()

    # Ověření, že je uživatel přesměrován na stránku '/cart.html'
    expect(
        page,
        "Uživatel nebyl správně přesměrován na stránku '/cart.html'."
    ).to_have_url("https://www.saucedemo.com/cart.html")

    # Iterace skrze předpřipravená testovací data PRODUCT_DATA
    for product in PRODUCT_DATA.values():
        # Najdeme konkrétní kontejner produktu v košíku podle jeho názvu
        cart_item = page.locator(".cart_item").filter(has_text=product["product_name"])

        # 1. Ověření, že se produkt nachází v košíku
        expect(
            cart_item,
            f"Produkt '{product['product_name']}' nebyl nalezen v detailu košíku."
        ).to_be_visible()
        
        # 2. Ověření, že se zobrazuje správné množství (1)
        quantity = cart_item.locator(".cart_quantity")
        expect(
            quantity,
            f"Produkt '{product['product_name']}' nemá očekávané množství '1'."
        ).to_have_text("1")
        
        # 3. Ověření, že se zobrazuje správný název produktu
        item_name = cart_item.locator(".inventory_item_name")
        expect(
            item_name,
            f"Název produktu neodpovídá očekávanému: '{product['product_name']}'."
        ).to_have_text(product["product_name"])

        # 4. Ověření zobrazení správné ceny
        item_price = cart_item.locator(".inventory_item_price")
        expect(
            item_price,
            f"Cena produktu '{product['product_name']}' neodpovídá očekávané hodnotě."
        ).to_have_text(f"${product['price']}")

        # 5. Ověření, že se zobrazuje tlačítko 'Remove'
        remove_btn = cart_item.locator(product["btn_selectors"]["remove_button"])
        expect(
            remove_btn,
            f"U produktu '{product['product_name']}' chybí tlačítko 'Remove'."
        ).to_be_visible()

    # Ověření, že se na stránce zobrazuje tlačítko 'Checkout'
    checkout_button = page.locator("#checkout")
    expect(
        checkout_button,
        "V detailu nákupního košíku chybí tlačítko 'Checkout'."
    ).to_be_visible()


@pytest.mark.parametrize("first_name, last_name, zip_code, error_message", [
    ("", "", "", "Error: First Name is required"),
    ("John", "", "", "Error: Last Name is required"),
    ("John", "Doe", "", "Error: Postal Code is required")
], ids=["TC04-1", "TC04-2", "TC04-3"])
def test_tc04_submit_invalid_order(auth_page_with_cart: Page, first_name: str, last_name: str, zip_code: str, error_message: str) -> None:
    """
    TC04: Odeslání chybně vyplněné objednávky
    Detail na testovací případ: ../docs/testovaci-pripady.md
    """
    page = auth_page_with_cart

    # Přechod na stránku nákupního košíku
    page.goto("https://www.saucedemo.com/cart.html")

    # 1. Kliknutí na tlačítko 'Checkout' a ověření přesměrování
    page.locator("#checkout").click()
    expect(
        page,
        "Uživatel nebyl přesměrován na stránku '/checkout-step-one.html'."
    ).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    # Ověření nadpisu stránky
    page_header_title = page.locator("#header_container > div.header_secondary_container > span")
    expect(
        page_header_title,
        "Na stránce se v nadpisu nezobrazuje očekávaný text 'Checkout: Your Information'."
    ).to_have_text("Checkout: Your Information")

    # Vyplnění objednávkového formuláře
    page.locator("#first-name").fill(first_name)
    page.locator("#last-name").fill(last_name)
    page.locator("#postal-code").fill(zip_code)
    page.locator("#continue").click()

    # Ověření zobrazení boxu s chybovou hláškou
    error_handler = page.locator(".error-message-container")
    expect(
        error_handler,
        "Na stránce se nezobrazil chybový box."
    ).to_be_visible()
    
    # Ověření správnosti samotného textu chybové hlášky
    expect(
        error_handler,
        f"V chybovém boxu se nezobrazuje očekávaná hláška: '{error_message}'."
    ).to_have_text(error_message)


def test_tc05_submit_order(auth_page_with_cart: Page) -> None:
    """
    TC05: Odeslání správně vyplněné objednávky
    Detail na testovací případ: ../docs/testovaci-pripady.md
    """
    page = auth_page_with_cart
    
    # Výchozí stav, uživatel se nachází na '/checkout-step-one.html'
    page.goto("https://www.saucedemo.com/checkout-step-one.html")

    # Validní vyplnění objednávkového formuláře
    page.locator("#first-name").fill(TC05_ORDER_DATA["first_name"])
    page.locator("#last-name").fill(TC05_ORDER_DATA["last_name"])
    page.locator("#postal-code").fill(TC05_ORDER_DATA["zip_code"])
    page.locator("#continue").click()

    # Ověření, že po úspěšném vyplnění formuláře je uživatel přesměrován na '/checkout-step-two.html'
    expect(
        page,
        "Uživatel po úspěšném vyplnění formuláře nebyl přesměrován na '/checkout-step-two.html'."
    ).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    # Výpočty cen objednávky 
    calculated_price = summary_price(product_test_data=PRODUCT_DATA, tax_rate=TAX_RATE)

    # Ověření ceny bez daně
    summary_without_tax = page.locator(".summary_subtotal_label")
    expect(
        summary_without_tax,
        "Na stránce se špatně zobrazuje výsledná cena objednávky bez daně."
    ).to_have_text(f"Item total: ${calculated_price['summary_price_without_tax']:.2f}")
    
    # Ověření výše započtené daně
    tax_label = page.locator(".summary_tax_label")
    expect(
        tax_label,
        "Na stránce je špatně uvedená výše daně."
    ).to_have_text(f"Tax: ${calculated_price['tax']:.2f}")

    # Ověření výsledné ceny se započtenou daní
    summary_with_tax = page.locator(".summary_total_label")
    expect(
        summary_with_tax,
        "Na stránce se špatně zobrazuje výsledná cena objednávky včetně daně."
    ).to_have_text(f"Total: ${calculated_price['summary_price_with_tax']:.2f}")

    # Potvrzení objednávky
    finish_btn = page.locator("#finish")
    expect(
        finish_btn,
        "Na stránce se nezobrazuje tlačítko pre odeslání objednávky."
    ).to_be_visible()

    finish_btn.click()

    # Ověření přesměrování po odeslání objednávky
    expect(
        page,
        "Uživatel po odeslání objednávky nebyl přesměrován na '/checkout-complete.html'."
    ).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    
    # Ověření úspěšného dokončení (Success message)
    title = page.locator(".complete-header")
    expect(
        title,
        "Na stránce se nezobrazuje text 'Thank you for your order!'."
    ).to_have_text("Thank you for your order!")

def test_tc06_logout_user(auth_page: Page) -> None:
    """
    TC06: Odhlášení uživatele z aplikace
    Detail na testovací případ: ../docs/testovaci-pripady.md
    """

    # Vyhledání a kliknutí na tlačítko menu
    menu_btn = auth_page.locator("#react-burger-menu-btn")
    expect(
        menu_btn,
        "Na stránce se nezobrazuje tlačítko pro zobrazení hlavního menu."
    ).to_be_visible()   
    menu_btn.click()

    # Ověření a kliknutí na tlačítko odhlášení (Playwright automaticky čeká, až bude plně viditelné a klikatelné)
    logout_btn = auth_page.locator("#logout_sidebar_link")
    expect(
        logout_btn,
        "V hlavním menu se nezobrazuje tlačítko pro odhlášení uživatele z aplikace."
    ).to_be_visible()
    logout_btn.click()

    # Ověření přesměrování na hlavní stránku aplikace
    expect(
        auth_page,
        "Uživatel po kliknutí na tlačítko odhlášení nebyl přesměrován na hlavní stránku aplikace."
    ).to_have_url("https://www.saucedemo.com/")


    # Bezpečnostní kontrola: Ověření, že se nepřihlášený uživatel nedostane zpět přes přímý odkaz
    auth_page.goto("https://www.saucedemo.com/inventory.html")

    expect(
        auth_page,
        "Nepřihlášený uživatel nebyl po pokusu o vstup na chráněnou stránku přesměrován na hlavní stránku."
    ).to_have_url("https://www.saucedemo.com/")

    # Ověření zobrazení chybového boxu s hláškou o odepření přístupu
    error_text = auth_page.locator("[data-test='error']")
    expect(
        error_text,
        "Na stránce se nezobrazil informační box s chybovou hláškou."
    ).to_be_visible()
    
    expect(
        error_text,
        "V informačním boxu se nenachází očekávaný text varování."
    ).to_have_text("Epic sadface: You can only access '/inventory.html' when you are logged in.")