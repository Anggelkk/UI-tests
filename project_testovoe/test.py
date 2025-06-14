from time import sleep

from project_testovoe.Home_page import HomePage
from project_testovoe.Search_page import SearchPage

def test_search_page(page):
    home_page = HomePage(page)
    home_page.open_homepage()
    home_page.homepage_verify()
    home_page.click_login_button()

    search_page = SearchPage(page)
    search_page.input_name()
    search_page.select_value()
    sleep(3)
    search_page.select_filter()
    sleep(3)
    search_page.select_min_sum_credit()
    sleep(3)
    search_page.click_button_search()
    sleep(3)


