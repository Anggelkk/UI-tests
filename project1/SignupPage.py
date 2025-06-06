from tkinter.font import names
from faker import Faker
from project1.BasePage import BasePage
import locator
from playwright.sync_api import Page, expect

fake = Faker()
Name = fake.name()
Email = fake.email()
Password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
class SignupPage(BasePage):
    def enter_name(self):
        self.page.is_visible("input[data-qa='signup-name']")
        self.page.fill("input[data-qa='signup-name']", Name)

    def enter_email(self):
        self.page.is_visible("input[data-qa='signup-email']")
        self.page.fill("input[data-qa='signup-email']", Email)

    def click_button(self):
        self.page.is_visible("button[data-qa='signup-button']")
        self.page.click("button[data-qa='signup-button']")

    def click_title(self):
        self.page.is_visible("input[id='id_gender2']")
        self.page.click("input[id='id_gender2']")

    def enter_password(self):
        self.page.is_visible("input[id='password']")
        self.page.fill("input[id='password']", Password)

    def test_month_dropdown(self):
        dropdown = self.page.locator("select[id='months']")

        assert dropdown.is_visible()

        # Проверка всех опций
        expected = [
            "Month", "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        assert dropdown.locator("option").all_text_contents() == expected

        # Выбор мая по тексту
        dropdown.select_option(label="May")
        assert dropdown.input_value() == "5"

        # Альтернатива: проверить текст
        selected = dropdown.locator("option[selected]").text_content()
        assert selected == "May"



    def test_days_dropdown(self):
        dropdown = self.page.locator("select[id='days']")

        assert dropdown.is_visible()

        expected_options = ["Day"] + [str(i) for i in range(1, 32)]
        actual_options = dropdown.locator("option").all_text_contents()
        print(actual_options)

        assert actual_options == expected_options

        dropdown.select_option(value="4")
        assert dropdown.input_value() == "4"

