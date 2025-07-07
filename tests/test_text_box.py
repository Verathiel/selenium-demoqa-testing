from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import unittest

class TextBoxTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # pro tichý režim
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://demoqa.com/text-box")
        self.driver.implicitly_wait(10)

    def test_fill_text_box(self):
        driver = self.driver

        driver.find_element(By.ID, "userName").send_keys("Veronika Tester")
        driver.find_element(By.ID, "userEmail").send_keys("veronika@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("Testovací 123")
        driver.find_element(By.ID, "permanentAddress").send_keys("Testland")
        driver.find_element(By.ID, "submit").click()

        output_name = driver.find_element(By.ID, "name").text
        output_email = driver.find_element(By.ID, "email").text

        self.assertIn("Veronika Tester", output_name)
        self.assertIn("veronika@example.com", output_email)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
