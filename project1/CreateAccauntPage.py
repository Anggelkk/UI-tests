from project1.BasePage import BasePage

class CreateAccountPage(BasePage):

    def click_button_continue(self):
        self.page.is_visible("a[data-qa='continue-button']")
        self.page.click("a[data-qa='continue-button']")
