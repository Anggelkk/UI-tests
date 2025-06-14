from time import sleep

from project2.Home_page import HomePage
from project2.Signin_page import SigninPage

def test_signin_page(page):

    home_page = HomePage(page)
    home_page.open_homepage()
    home_page.homepage_verify()
    home_page.click_login_button()

    signin_page = SigninPage(page)
    signin_page.input_name()
    signin_page.input_email()
    signin_page.click_button_signup()
    signin_page.input_title()
    signin_page.input_pass()
    signin_page.select_days()
    signin_page.select_month()
    signin_page.select_years()
    sleep(5)