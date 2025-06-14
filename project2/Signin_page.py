from playwright.sync_api import expect

from project2.Base_page import BasePage

name = "Angelina"
email = "lina@yandex.ru"
password = "12345678"
class SigninPage(BasePage):

    """Enter Account Information"""
    def input_name(self):
        self.page.is_visible("input[data-qa='signup-name']")
        self.page.fill("input[data-qa='signup-name']", name)

    def input_email(self):
        self.page.is_visible("input[data-qa='signup-email']")
        self.page.fill("input[data-qa='signup-email']",email)

    def click_button_signup(self):
        self.page.is_visible("button[data-qa='signup-button']")
        self.page.click("button[data-qa='signup-button']")

    def input_title(self):
        self.page.is_visible("input[id='id_gender2']")
        self.page.click("input[id='id_gender2']")

    def input_pass(self):
        self.page.is_visible("input[data-qa='password']")
        self.page.fill("input[data-qa='password']",password)

    def select_days(self):
        dropdown = self.page.locator("select[id='days']")

        expected_actual = dropdown.locator("option").all_text_contents()
        print(expected_actual)
        expected_value = ["Day"] + [str(i) for i in range(1,32)]
        print(expected_value)

        assert expected_actual == expected_value

        dropdown.select_option(value="13")
        assert dropdown.input_value() == "13"

    def select_month(self):
        dropdown = self.page.locator("select[id='months']")

        expected_actual = ["January", "February", "March","April","May","June","July","August","September","October", "November","December"]
        expected_value = [str(i) for i in expected_actual]

        assert expected_actual == expected_value
        dropdown.select_option(value="July")

    def select_years(self):
        dropdown = self.page.locator("select[data-qa='years']")
        expect(dropdown).to_be_visible()

        expected_options = ["Year"] + [str(i) for i in range(2021, 1899, -1)]
        actual_options = dropdown.locator("option").all_text_contents()

        assert expected_options == actual_options
        dropdown.select_option(value=expected_options)

