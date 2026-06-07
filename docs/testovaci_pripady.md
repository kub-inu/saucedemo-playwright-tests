# Testovací případy

| ID | Název testu | Priorita | Typ testu |
| :--- | :--- | :--- | :--- |
| **TC01** | Úspěšné přihlášení uživatele | P0 - Kritická | Pozitivní funkční test (Happy Path) |
| **TC02** | Přidání produktu do nákupního košíku | P1 - Vysoká | Pozitivní funkční test |
| **TC03** | Ověření detailu obsahu nákupního košíku | P1 - Vysoká | Pozitivní funkční test (Validace dat) |
| **TC04** | Odeslání chybně vyplněné objednávky | P2 - Střední | Negativní test (Data-Driven) |
| **TC05** | Odeslání správně vyplněné objednávky | P0 - Kritická | End-to-End (E2E / Happy Path) |
| **TC06** | Odhlášení uživatele z aplikace | P2 - Střední | Pozitivní funkční test |

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



## TC03: Ověření detailu obsahu nákupního košíku
Ověření, že po zobrazení obsahu nákupního košíku na stránce `/cart.html` se zobrazí správné informace o produktech v košíku.

**Předpoklady**
- Uživatel je přihlášen jako: `standard_user`
- Uživatel má v nákupním košíku 2 produkty: `Sauce Labs Backpack` a `Sauce Labs Bike Light`

**Testovací data**
- Uložené produkty v nákupním košíku

**Kroky testu**
1. Na stránce `inventory.html` stiskni ikonu nákupního košíku.
2. Ověř, že došlo k přesměrování na podstránku: `https://www.saucedemo.com/cart.html`
3. Ověř, že se v seznamu zobrazují uložené produkty z nákupního košíku:
    1. Ověř, že se vypisuje správný název produktu.
    2. Ověř, že se vypisuje správný popis produktu.
    3. Ověř, že se vypisuje správná cena produktu.
    4. Ověř, že se u produktu nachází tlačítko `Remove`.
4. Ověř, že se na stránce nachází tlačítko `Checkout` pro pokračování v objednávce.

**Očekávaný výsledek**
- V detailu nákupního košíku se zobrazují všechny uložené produkty: `Sauce Labs Backpack` a `Sauce Labs Bike Light`.
- U jednotlivých produktů je správně uveden název, popis, cena a položky obsahují tlačítko `Remove` pro odstranění ze seznamu.
- Z detailu košíku je možné dále pokračovat k vyplnění objednávky pomocí tlačítka `Checkout`.



## TC04: Odeslání chybně vyplněné objednávky
Testování, zda se po zadání neúplných údajů do formuláře zobrazí správná chybová hláška a uživatel není přesměrován dále.

**Předpoklady**
- Uživatel je přihlášen jako: `standard_user`
- Uživatel má v nákupním košíku uložené dva produkty: `Sauce Labs Backpack` a `Sauce Labs Bike Light`
- Uživatel se nachází na stránce: `https://www.saucedemo.com/cart.html`

**Testovací sada**
| ID | Popis | Data | Chybová hláška | 
| :--- | :--- | :--- | :--- |
| TC04-1 | Pokus o odeslání zcela nevyplněného formuláře | First Name: `""`; Last Name: `""`; Zip Code: `""` | `Error: First Name is required` |
| TC04-2 | Pokus o odeslání formuláře bez příjmení a PSČ | First Name: `John`; Last Name: `""`; Zip Code: `""` | `Error: Last Name is required` |
| TC04-3 | Pokus o odeslání formuláře bez PSČ | First Name: `John`; Last Name: `Doe`; Zip Code: `""` | `Error: Postal Code is required` |

**Kroky testu**
1. Klikni na tlačítko `Checkout`.
2. Ověř, že uživatel je přesměrován na podstránku: `https://www.saucedemo.com/checkout-step-one.html` a nadpis stránky (title) zobrazuje: `Checkout: Your Information`.
3. Objednávkový formulář vyplň podle dat z vybraného řádku testovací sady a stiskni tlačítko `Continue`.
4. Ověř, že se zobrazí chybová hláška a její obsah je shodný s textem v testovací sadě.
5. Ověř, že uživatel zůstal na stránce `/checkout-step-one.html`.
6. Ověř, že číslo u ikony nákupního košíku stále zobrazuje hodnotu 2.
7. (Pro automatizaci: Kroky 3–6 se opakují samostatně pro každý řádek z testovací sady).

**Očekávaný výsledek**
- Formulář se neodešle a uživatel nadále zůstává na stránce `/checkout-step-one.html`.
- Systém správně reaguje na chybějící údaje a zobrazuje odpovídající chybové hlášky podle testovací sady.
- Obsah košíku zůstává nezměněn (stále obsahuje 2 položky).


## TC05: Odeslání správně vyplněné objednávky
Ověření, že po zadání platných údajů do formuláře se zobrazí rekapitulace se správnou výslednou cenou a uživatel může objednávku úspěšně dokončit.

**Předpoklady**
- Uživatel je přihlášen jako: `standard_user`
- Uživatel má v nákupním košíku uložené dva produkty (`Sauce Labs Backpack` a `Sauce Labs Bike Light`)
- Uživatel se nachází na stránce: `https://www.saucedemo.com/checkout-step-one.html`

**Testovací data**
- First Name: `John`, Last Name: `Doe`, Zip Code: `12345`

**Kroky testu**
1. Do formuláře zadej hodnoty `John`, `Doe`, `12345` a stiskni tlačítko `Continue`.
2. Ověř, že je uživatel přesměrován na stránku: `https://www.saucedemo.com/checkout-step-two.html`.
3. Ověř, že celková cena včetně daně odpovídá hodnotě `Total: $43.18`.
4. Stiskni tlačítko `Finish`.
5. Ověř, že je uživatel přesměrován na finální stránku: `https://www.saucedemo.com/checkout-complete.html`.
6. Ověř, že se na stránce zobrazí potvrzení `Thank you for your order!` a ikona nákupního košíku je prázdná.

**Očekávaný výsledek**
- Uživatel úspěšně projde rekapitulací se správně spočítanou výslednou cenou, objednávku dokončí a košík se vyprázdní.



## TC06: Odhlášení uživatele z aplikace
Ověření, že se přihlášený uživatel může bezpečně odhlásit z aplikace přes hlavní menu a je přesměrován zpět na přihlašovací stránku.

**Předpoklady**
- Uživatel je přihlášen jako: `standard_user`
- Uživatel se nachází na libovolné interní stránce e-shopu (např. `/inventory.html`)

**Kroky testu**
1. Klikni na navigační menu vlevo nahoře (ikona se třemi vodorovnými čárkami).
2. V otevřeném bočním panelu klikni na odkaz `Logout`.
3. Ověř, že je uživatel přesměrován na úvodní stránku: `https://www.saucedemo.com/`.
4. Ověř, že přihlašovací pole `Username` a `Password` jsou prázdná.

**Očekávaný výsledek**
- Systém uživatele úspěšně odhlásí, zruší jeho relaci a vrátí ho na čistou přihlašovací obrazovku.