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

## Nastavení projektu

1. Vytvoř a aktivuj virtuální prostředí:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Nainstaluj závislosti:

    ```bash
    pip install -r requirements.txt
    ```

3. Ujisti se, že máš `chromedriver` v PATH  
   (nebo uprav pevnou cestu v testu `tests/test_text_box.py`).  

---

## Spuštění testů

```bash
python3 -m pytest tests/
Struktura projektu
bash
Zkopírovat
Upravit
.
├── pages/               # Page Object model pro Text Box
│   └── text_box_page.py
├── tests/               # Testovací skripty
│   └── test_text_box.py
├── requirements.txt     # Seznam Python závislostí
└── README.md            # Tento popis projektu
Automatické testování (CI/CD)
Projekt využívá GitHub Actions pro automatické spouštění testů při každém pushi nebo pull requestu do větve main:

Používá se Python 3.9

Instalují se závislosti ze souboru requirements.txt

Testy se spouštějí pomocí pytest

Výsledky testů jsou viditelné přímo v záložce Actions na GitHubu

Díky tomu je zajištěno, že každý nový kód prochází automatickou kontrolou funkčnosti a projekt zůstává stabilní.

