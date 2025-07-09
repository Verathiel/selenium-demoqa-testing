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
        submit_btn = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   submit_btn)
        submit_btn.click()

    def get_output_name(self):
        return self.driver.find_element(*self.output_name).text

    def get_output_email(self):
        return self.driver.find_element(*self.output_email).text
