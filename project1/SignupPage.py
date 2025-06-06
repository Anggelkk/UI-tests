from tkinter.font import names
from faker import Faker
from project1.BasePage import BasePage
import locator
from playwright.sync_api import Page, expect

fake = Faker()
Name = fake.name()
Email = fake.email()
Month = fake.month_name()
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

        dropdown.select_option(label="May")
        assert dropdown.input_value() == "5"

    def test_days_dropdown(self):
        dropdown = self.page.locator("select[id='days']")

        assert dropdown.is_visible()

        expected_options = ["Day"] + [str(i) for i in range(1, 32)]
        print(expected_options)
        actual_options = dropdown.locator("option").all_text_contents()
        print(actual_options)

        assert actual_options == expected_options

        """Выборка конкретного дня"""
        # dropdown.select_option(value="4")
        # assert dropdown.input_value() == "4"

        """Выборка рандомного дня"""
        random_day_int = fake.random_int(min=1, max=31)
        random_day_str = str(random_day_int)

        dropdown.select_option(value=random_day_str)

        assert dropdown.input_value() == random_day_str


    def test_years_dropdown(self):
        dropdown = self.page.locator("select[id='years']")

        assert dropdown.is_visible()

        expected_option = ["Year"] + [str(i) for i in range(2021, 1899, -1)]
        print(expected_option)
        actual_options = dropdown.locator("option").all_text_contents()
        print(actual_options)

        assert actual_options == expected_option

        """Выборка конкретной даты"""
        # dropdown.select_option(value="2020")
        # assert dropdown.input_value() == "2020"

        """Выборка рандомной даты"""
        random_year_int = fake.random_int(min=1900, max=2021)
        random_year_str = str(random_year_int)
        dropdown.select_option(value=random_year_str)

        assert dropdown.input_value() == random_year_str  # Проверяем value
