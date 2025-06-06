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
    signup_page.test_years_dropdown()
    sleep(5)

