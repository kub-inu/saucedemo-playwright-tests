# Testovací případy

## TC01: Úspěšné přihlášení uživatele
Ověření, že po zadání platných přihlašovacích údajů se uživatel přihlásí, je přesměrován na stránku `/inventory.html` a zobrazí se mu seznam produktů e-shopu.

**Testovací data**
- Přihlašovací jméno: `standard_user`
- Heslo: `secret_sauce`

**Kroky testu**
1. Přejdi na stránku: `https://www.saucedemo.com/`
2. Do pole `Username` zadej hodnotu: `standard_user`
3. Do pole `Password` zadej hodnotu: `secret_sauce`
4. Stiskni tlačítko: `Login`

**Očekávaný výsledek**
- Přihlášení je úspěšné a uživatel je přesměrován na URL: `https://www.saucedemo.com/inventory.html`
- Na stránce se zobrazí seznam produktů z e-shopu.


## TC02: Přidání produktu do nákupního košíku
Ověření, že uživatel je schopen přidat jeden nebo více produktů do nákupního košíku.

**Předpoklady**
- Uživatel je přihlášen jako: `standard_user`
- Uživatel se nachází na stránce: `https://www.saucedemo.com/inventory.html`

**Testovací data**
- Seznam produktů e-shopu (min. 2 produkty)
- Produkty: `Sauce Labs Backpack`, `Sauce Labs Bike Light`

**Kroky testu**
1. U produktu `Sauce Labs Backpack` stiskni tlačítko `Add to cart`.
2. Ověř, že se text tlačítka změnil na `Remove`.
3. Ověř, že se u ikony nákupního košíku zobrazí číslo 1.
4. Akci zopakuj a u produktu `Sauce Labs Bike Light` stiskni tlačítko `Add to cart`.
5. Ověř, že se text druhého tlačítka změnil na `Remove`.
6. Ověř, že se u ikony nákupního košíku zobrazí číslo 2.

**Očekávaný výsledek**
- Oba produkty se přidají do nákupního košíku – u ikony nákupního košíku se zobrazuje číslo 2.
- Tlačítko `Add to cart` se po stisknutí změní na text: `Remove`.