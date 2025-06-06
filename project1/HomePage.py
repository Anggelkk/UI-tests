from project1.BasePage import BasePage


class HomePage(BasePage):
    def open_homepage(self):
        self.page.goto('https://automationexercise.com')

    def verify_homepage(self):
        self.page.wait_for_load_state("load", timeout=20000)

    def click_login_button(self):
        self.page.is_visible("a[href='/login']")
        self.page.click("a[href='/login']")