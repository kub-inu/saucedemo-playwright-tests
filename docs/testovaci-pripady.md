# Testovací případy

## TC01: Úspěšné přihlášení uživatele
Ověření, že po zadaní platních přihlasovacích udajů se uživatel přihlási a je presmerován na stránku `/inventory.html` a zobrazí sa mu seznam produktů e-shopu.

**Testovací data**
- Přihlasovací jméno: `standard_user`
- Heslo: `secret_sauce`

**Kroky testu**
1. Přejdi na stránku: `https://www.saucedemo.com/`
2. Do pole `Username` zadej hodnotu: `standard_user`
3. Do pole `Password` zadej hodnotu: `secret_sauce`
4. Stiskni tlačidlo: `Login`

**Očekávaný výsledek**
- Přihlášení je úspěšné a uživatel je přesmerován na URL: `https://www.saucedemo.com/inventory.html`
- Na stránce se zobrazí seznam produků z eshopu


## TC02: Přidání produktu do nákupního košíku
Ověření, že uživatel je schopen přidat jeden nebo více produktů do nákupního košíku.

**Předpodmínky**
- Uživatel je přihlášen jako: `standard_user`
- Uživatel se nachází na stránce: `https://www.saucedemo.com/inventory.html/`

**Testovací data**
- Seznam prodktů e-shopu (min. 2 produkty)
- Produkty: `Sauce Labs Backpack`, `Sauce Labs Bike Light`

**Kroky testu**
1. U produktu `Sauce Labs Backapack` stiskni tlačidlo `Add to card`.
2. Ověř, že se text tlačidla změnil na `Remove`.
3. Ověř, že při ikone nákupního košíku se zobrazí číslo 1.
4. Akci zopakuj a při produkte `Sauce Labs Bike Light` stiskni tlačidlo `Add to card`.
5. Ověř, že se text druhého tlačidla změnil na `Remove`.
6. Ověř, že se při ikone nákupního košíku zobrazí číslo 2.

**Očekávaný výsledek**
- Oba produkty se přidají do nákupního košíku - při ikone nákupního košíku se zobrazuje číslo 2
- Tlačidlo `Add to card` se po stisknutí změní na červené tlačidlo s textem: `Remove`

