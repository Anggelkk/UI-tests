import random
from tabnanny import check
from tkinter.font import names
from faker import Faker
from project1.BasePage import BasePage
import locator
from playwright.sync_api import Page, expect

fake = Faker()
Name = fake.name()
LastName = fake.name()
Email = fake.email()
Password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
Company = 'MSB'
State = 'Russia'
Address = fake.address()
City = fake.city()
Zipcode = fake.zipcode()
MobileNumber = '+79511463645'

class SignupPage(BasePage):

    """ENTER ACCOUNT INFORMATION"""
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

        actual_labels = dropdown.locator("option").all_text_contents()
        # Получаем все <option> элементы и их атрибуты 'value'
        actual_values = [
            option.get_attribute("value") for option in dropdown.locator("option").all()
        ]

        """рандомный подбор месяца"""
        expected = [
            "Month", "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

        expected_values = [""] + [f"{i}" for i in range(1, 13)]
        assert actual_labels == expected
        assert actual_values == expected_values

        random_month_int = fake.random_int(min=1, max=12)
        random_month_value_str = f"{random_month_int:1d}"

        dropdown.select_option(value=random_month_value_str)

        assert dropdown.input_value() == random_month_value_str

        """Конкретный месяц"""
        # dropdown.select_option(label="May")
        # assert dropdown.input_value() == "5"


    def test_days_dropdown(self):
        dropdown = self.page.locator("select[id='days']")

        assert dropdown.is_visible()

        expected_options = ["Day"] + [str(i) for i in range(1, 32)]
        actual_options = dropdown.locator("option").all_text_contents()


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
        actual_options = dropdown.locator("option").all_text_contents()


        assert actual_options == expected_option

        """Выборка конкретной даты"""
        # dropdown.select_option(value="2020")
        # assert dropdown.input_value() == "2020"

        """Выборка рандомной даты"""
        random_year_int = fake.random_int(min=1900, max=2021)
        random_year_str = str(random_year_int)
        dropdown.select_option(value=random_year_str)

        assert dropdown.input_value() == random_year_str

    def click_div_first(self):
        checkbox_newsletter = self.page.locator("input#newsletter")
        expect(checkbox_newsletter).to_be_visible()
        checkbox_newsletter.check()
        expect(checkbox_newsletter).to_be_checked()

    def click_div_second(self):
        checkbox_optin = self.page.locator("input#optin")
        expect(checkbox_optin).to_be_visible()
        checkbox_optin.check()
        expect(checkbox_optin).to_be_checked()

    """ADDRESS INFORMATION"""

    def input_first_name(self):
        self.page.is_visible("input[id='first_name']")
        self.page.fill("input[id='first_name']", Name)

    def input_last_name(self):
        self.page.is_visible("input[id='last_name']")
        self.page.fill("input[id='last_name']", LastName)

    def input_company(self):
        self.page.is_visible("input[id='company']")
        self.page.fill("input[id='company']", Company)

    def input_address(self):
        self.page.is_visible("input[id='address1']")
        self.page.fill("input[id='address1']", Address)

    def input_address2(self):
        self.page.is_visible("input[id='address2']")
        self.page.fill("input[id='address2']", Address)

    def select_country(self):
        dropdown = self.page.locator("select[id='country']")
        dropdown.is_visible()

        actual_labels = dropdown.locator("option").all_text_contents()
        actual_values = [option.get_attribute('value') for option in dropdown.locator("option").all()]
        print(actual_labels)
        print(actual_values)
        expected = ["India","United States", "Canada", "Australia", "Israel", "New Zealand", "Singapore"]
        expected_values = ["India","United States", "Canada", "Australia", "Israel", "New Zealand", "Singapore"]
        print(expected)
        print(expected_values)

        assert expected == actual_labels
        assert expected_values == actual_values

        random_country_to_select = fake.random.choice(actual_labels)
        dropdown.select_option(value=random_country_to_select)

        assert dropdown.input_value() == random_country_to_select

    def input_state(self):
        self.page.is_visible("input[id='state']")
        self.page.fill("input[id='state']", State)

    def input_city(self):
        self.page.is_visible("input[id='city']")
        self.page.fill("input[id='city']", City)

    def input_zipcode(self):
        self.page.is_visible("input[id='zipcode']")
        self.page.fill("input[id='zipcode']", Zipcode)

    def input_mobile(self):
        self.page.is_visible("input[id='mobile_number']")
        self.page.fill("input[id='mobile_number']", MobileNumber)

    def click_button_create_acc(self):
        self.page.is_visible("button[data-qa='create-account']")
        self.page.click("button[data-qa='create-account']")