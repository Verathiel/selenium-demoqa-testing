# Selenium Test: Text Box Formulář (DemoQA)

Tento projekt automatizovaně testuje **formulář na stránce [demoqa.com/text-box](https://demoqa.com/text-box)** pomocí **Pythonu**, **Selenium WebDriveru** a **Pytestu**.

---

## Co test ověřuje

- Otevření stránky s formulářem
- Vyplnění polí:  
  `Jméno`, `E-mail`, `Aktuální adresa`, `Trvalá adresa`
- Odeslání formuláře
- Ověření, že se zadané hodnoty správně zobrazí na výstupu

---

## Požadavky

- Python **3.9+**
- ChromeDriver (**verze odpovídající tvému Chrome prohlížeči**) v PATH
- Virtuální prostředí (doporučeno)

---

##  Nastavení projektu

1. Vytvoř a aktivuj virtuální prostředí:

```bash
python3 -m venv venv
source venv/bin/activate
Nainstaluj závislosti:

bash
Zkopírovat
Upravit
pip install -r requirements.txt
Ujisti se, že máš chromedriver v PATH
(nebo uprav pevnou cestu v testu test_text_box.py).

Spuštění testů
bash
Zkopírovat
Upravit
python3 -m pytest tests/
Struktura projektu
bash
Zkopírovat
Upravit
.
├── pages/               # Page Object pro Text Box
│   └── text_box_page.py
├── tests/               # Testovací skript
│   └── test_text_box.py
├── requirements.txt     # Seznam závislostí
└── README.md            # Tento popis projektu
