from project2.Base_page import BasePage

class HomePage(BasePage):
    def open_homepage(self):
        self.page.goto('http://automationexercise.com')

    def homepage_verify(self):
        self.page.wait_for_load_state("load", timeout=5000)

    def click_login_button(self):
        self.page.is_visible("a[href='/login']")
        self.page.click("a[href='/login']")