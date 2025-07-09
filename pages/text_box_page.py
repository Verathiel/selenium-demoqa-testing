from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TextBoxPage:

    def __init__(self, driver):
        self.driver = driver
        self.user_name_input = (By.ID, "userName")
        self.user_email_input = (By.ID, "userEmail")
        self.current_address_textarea = (By.ID, "currentAddress")
        self.permanent_address_textarea = (By.ID, "permanentAddress")
        self.submit_button = (By.ID, "submit")
        self.output_name = (By.ID, "name")
        self.output_email = (By.ID, "email")

    def open(self):
        self.driver.get("https://demoqa.com/text-box")

    def fill_form(self, name, email, current_address, permanent_address):
        self.driver.find_element(*self.user_name_input).send_keys(name)
        self.driver.find_element(*self.user_email_input).send_keys(email)
        self.driver.find_element(
            *self.current_address_textarea).send_keys(current_address)
        self.driver.find_element(
            *self.permanent_address_textarea).send_keys(permanent_address)

    def submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_output_name(self):
        return self.driver.find_element(*self.output_name).text

    def get_output_email(self):
        return self.driver.find_element(*self.output_email).text


# --- Kód pro spuštění testu / demo ---
if __name__ == "__main__":
    chrome_driver_path = "/nix/store/3w27rhw8rwxhf915b7gqlflf02cnqbjv-chromedriver-92.0.4515.107/bin/chromedriver"
    service = Service(executable_path=chrome_driver_path)

    options = Options()
    # options.add_argument("--headless")  # Tohle vynecháme, chceme vidět okno
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=service, options=options)

    page = TextBoxPage(driver)
    page.open()
    page.fill_form("Veronika", "veronika@example.com", "Moje adresa 123",
                   "Jiná adresa 456")
    page.submit()

    print("Výstup jméno:", page.get_output_name())
    print("Výstup email:", page.get_output_email())

    driver.quit()
