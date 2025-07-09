import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.text_box_page import TextBoxPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # běh bez okna prohlížeče
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_fill_text_box(driver):
    page = TextBoxPage(driver)
    page.open()
    page.fill_form("Veronika Tester", "veronika@example.com", "Testovací 123", "Testland")
    page.submit()

    assert "Veronika Tester" in page.get_output_name()
    assert "veronika@example.com" in page.get_output_email()
