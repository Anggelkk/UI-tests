from time import sleep

from project1.HomePage import HomePage
from project1.SignupPage import SignupPage

def test_open_page(page):
    home_page = HomePage(page)
    home_page.open_homepage()
    home_page.verify_homepage()

def test_register_user(page):
    home_page = HomePage(page)
    home_page.open_homepage()
    home_page.verify_homepage()
    home_page.click_login_button()
    print(home_page)

    signup_page = SignupPage(page)
    signup_page.enter_name()
    signup_page.enter_email()
    signup_page.click_button()
    signup_page.click_title()
    signup_page.enter_password()
    signup_page.test_month_dropdown()
    signup_page.test_days_dropdown()
    sleep(5)

    # def test_days_dropdown(self):
    #     dropdown = self.page.locator("select[id='days']")
    #
    #     assert dropdown.is_visible()
    #
    #     expected = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    #
    #
    #     assert dropdown.locator("option") == expected
    #     dropdown.select_option(label= "4")
    #     assert dropdown.input_value() == "4"
    #
    #     selected = dropdown.locator("option[selected]").text_content()
    #     assert selected == '4'