# SauceDemo E-shop - Playwright automatizované testy

Závěrečný projekt kurzu **Testing Akademie od Engeta**. Zadáním projektu bylo vytvoření tří automatizovaných skriptů webové stránky podle vlastního výběru.

V závěrečném vypracování projektu jsem zadání rozšířil a vytvořil **6 komplexních automatizovaných testů**, které pokrývají E2E (End-to-End) scénář testovaného e-shopu: od úspěšného přihlášení, přes přidání produktu do nákupního košíku a validaci cen v checkout procesu, až po odeslání objednávky a odhlášení.


## Informace o projektu

### Testovaný objekt

| Název | Detaily |
| :--- | :--- |
| **URL** | [https://www.saucedemo.com](https://www.saucedemo.com) |
| **Testovací účet** | `standard_user` |

### Rozsah testování

Vzhledem k prokázání schopnosti používání nástrojů pro automatizované testování a podmínce tří automatizovaných testů je rozsah testování zúžen na kriticky důležité funkcionality e-shopu pro úspěšné ověření E2E toku.

**V testování je zahrnuto:**

1. Přihlášení uživatele s validními údaji.
2. Vložení produktu do košíku.
3. Ověření, že se produkt nachází a správně zobrazuje v košíku.
4. Negativní testování checkout formuláře s nevyplněnými povinnými poli.
5. Úspěšné odeslání objednávky včetně dynamického dopočtu cen a daně.
6. Odhlášení uživatele a neautentizovaný pokus o přímý vstup do aplikace.

**Mimo rozsah testování:**

Netestovaly se ostatní případy typu hraniční testování vložených hodnot formuláře, bezpečnostní/penetrační testování, výkonnost aplikace a podobně.

### Metodika testování

V testovacích skriptech je využito:

- **Pozitivní a negativní testování** – ověření správného chování systému při korektních i nekorektních vstupech.
- **Parametrizované testování (Data-Driven Testing)** – efektivní ověřování více scénářů bez duplicity kódu, využito při validaci formuláře.
- **End-to-End (E2E) testování** – simulace kompletního průchodu reálného uživatele systémem.

---

## Použité technologie

| Název | Verze | Shrnutí |
| :--- | :--- | :--- |
| **Python** | `v3.14.*` | Programovací jazyk, ve kterém je napsané celé testovací řešení. |
| **pytest** | `v9.*.*` | Testovací runner a knihovna pro řízení testů a parametrizaci. |
| **playwright** | `v1.60.0` | Framework pro automatizaci webových prohlížečů. |
| **pytest-html** | `v4.0.0` | Knihovna pro automatické generování HTML reportů. |


## Struktura projektu

```text
engeto-automatizace/
├── docs/
│   ├── report.html             -> HTML report vygenerovaný pytestem
│   └── testovaci_pripady.md    -> Detailní popis exekuovaných testovacích případů
│
├── src/
│   ├── helpers.py              -> Pomocné funkce využité v testech, např. výpočet sumy a daně
│   └── test_data.py            -> Izolovaná testovací data a konfigurace produktů
│
├── .gitignore
├── README.md
├── conftest.py                 -> Globální pytest fixtures, např. příprava přihlášeného stavu
├── test_saucedemo.py           -> Soubor se samotnými automatizovanými testy
└── requirements.txt            -> Soubor se závislostmi projektu pro pip
```



## Instalace a spuštění testů

Před instalací je nutné mít v počítači nainstalovaný Python `v3.*.*`.

### 1. Naklonování repozitáře

Otevřete terminál a naklonujte si projekt z GitHubu:

```bash
git clone https://github.com/kub-inu/engeto-automatizace.git
cd engeto-automatizace
```

### 2. Instalace závislostí

Nainstalujte potřebné balíčky ze souboru `requirements.txt` a stáhněte jádra prohlížečů pro Playwright:

```bash
pip install -r requirements.txt
playwright install
```

### 3. Spuštění testů

Testovací sadu je možné spustit přímo přes `pytest`:

```bash
pytest test_saucedemo.py
```

Nebo jako Python modul:

```bash
python -m pytest test_saucedemo.py
```

### 4. Spuštění testů s HTML reportem

Po doběhnutí testů se vygeneruje vizuální report do složky `docs/`.

```bash
pytest test_saucedemo.py --html=docs/report.html --self-contained-html
```

Nebo jako Python modul:

```bash
python -m pytest test_saucedemo.py --html=docs/report.html --self-contained-html
```


## Výstupy projektu

Projekt obsahuje tyto výstupy:

- automatizované testy v souboru `test_saucedemo.py`,
- testovací data v souboru `src/test_data.py`,
- pomocné funkce v souboru `src/helpers.py`,
- pytest fixtures v souboru `conftest.py`,
- dokumentované testovací případy v souboru `docs/testovaci_pripady.md`,
- HTML report v souboru `docs/report.html`.

