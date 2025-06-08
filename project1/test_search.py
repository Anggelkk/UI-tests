from time import sleep

from project1.CreateAccauntPage import CreateAccountPage
from project1.DeletePage import DeletePage
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
    signup_page.click_div_first()
    signup_page.click_div_second()

    signup_page.input_first_name()
    signup_page.input_last_name()
    signup_page.input_company()
    signup_page.input_address()
    signup_page.input_address2()
    signup_page.select_country()
    signup_page.input_state()
    signup_page.input_city()
    signup_page.input_zipcode()
    signup_page.input_mobile()
    signup_page.click_button_create_acc()

    create_account_page = CreateAccountPage(page)
    create_account_page.click_button_continue()

    delete_account_page = DeletePage(page)
    delete_account_page.delete_page()
    delete_account_page.click_continue_delete()
    sleep(6)
