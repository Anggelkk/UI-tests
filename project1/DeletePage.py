from project1.BasePage import BasePage

class DeletePage(BasePage):
    def delete_page(self):
        self.page.is_visible("a[href='/delete_account']")
        self.page.click("a[href='/delete_account']")

    def click_continue_delete(self):
        self.page.is_visible("a[class='btn btn-primary']")
        self.page.click("a[class='btn btn-primary']")