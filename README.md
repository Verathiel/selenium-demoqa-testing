# Selenium Test – DemoQA Text Box

Tento projekt demonstruje **automatizovaný test webového formuláře** pomocí Selenium WebDriver a Pythonu. Test ověřuje funkčnost textových polí na stránce [https://demoqa.com/text-box](https://demoqa.com/text-box) a je navržen tak, aby běžel v tichém („headless“) režimu, vhodném pro CI/CD prostředí.

---

## Co test kontroluje

Test vyplňuje následující pole formuláře:

- Full Name
- Email
- Current Address
- Permanent Address

Poté klikne na **Submit** a ověřuje, zda se zadaná data správně zobrazí v části výstupu.

---

## 🛠Instalace a spuštění

1. Naklonuj si repozitář:
```bash
git clone https://github.com/Verathiel/selenium-demoqa-testing.git
cd selenium-demoqa-testing
Nainstaluj požadované balíčky:

bash
Zkopírovat
Upravit
pip install -r requirements.txt
Spusť test:

bash
Zkopírovat
Upravit
python test_text_box.py
Test se spouští v tichém režimu pomocí --headless Chrome.

Struktura projektu
bash
Zkopírovat
Upravit
selenium-demoqa-testing/
├── test_text_box.py        # Testovací skript v Pythonu
├── requirements.txt        # Seznam závislostí
└── README.md               # Tento popis projektu
Použité technologie
Python

Selenium WebDriver

Unittest

ChromeDriver (v headless módu)

Autorka
Veronika Flachsová
Junior QA Tester & začínající Python programátorka

