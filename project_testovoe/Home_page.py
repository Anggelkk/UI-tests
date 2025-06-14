from project2.Base_page import BasePage

class HomePage(BasePage):
    def open_homepage(self):
        self.page.goto('http://37.203.243.26:5000')

    def homepage_verify(self):
        self.page.wait_for_load_state("load", timeout=5000)

    def click_login_button(self):
        self.page.is_visible("a[href='/search']")
        self.page.click("a[href='/search']")