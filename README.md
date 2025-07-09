# Testování Text Box Formuláře pomocí Selenium a Pytest

Tento projekt automatizovaně testuje formulář na stránce [https://demoqa.com/text-box](https://demoqa.com/text-box) pomocí Pythonu, Selenium WebDriveru a testovacího frameworku Pytest.

---

## Funkce testu

- Otevření stránky s formulářem
- Vyplnění polí: jméno, e-mail, aktuální adresa, trvalá adresa
- Odeslání formuláře
- Ověření, že se na výstupu zobrazí správné zadané hodnoty

---

## Požadavky

- Python 3.9+
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (verze odpovídající tvému Chrome prohlížeči) v PATH
- Virtuální prostředí (doporučeno)

---

## Nastavení projektu

1. Vytvoř a aktivuj virtuální prostředí:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
Nainstaluj závislosti:

bash
Zkopírovat
Upravit
pip install -r requirements.txt
Ujisti se, že máš chromedriver v PATH nebo nastav jeho cestu v testech.

Spuštění testů
Spustíš jednoduše příkazem:

bash
Zkopírovat
Upravit
python3 -m pytest tests/
Struktura projektu
pages/ - stránka s Page Object modelem pro Text Box formulář

tests/ - testovací skripty

requirements.txt - seznam Python závislostí

venv/ - virtuální prostředí (není v repozitáři)
