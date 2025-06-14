from project_testovoe.Base_page import BasePage
from faker import Faker

fake = Faker()
test_name = "Lina"
min_sum_credit = "50000"

class SearchPage(BasePage):
    def input_name(self):
        self.page.is_visible("input[id='query']")
        self.page.fill("input[id='query']", test_name)

    def select_value(self):
        dropdown = self.page.locator("select[id='sort_by']")

        """Конкретное значение"""
        actual_options = ["-- Выберите --", "По имени", "По сумме кредита", "По статусу", "Удалить все"]
        print(actual_options)
        expected_options = dropdown.locator("option").all_text_contents()
        print(expected_options)

        assert actual_options == expected_options
        dropdown.select_option(value="По имени")

    def select_filter(self):
        self.page.is_visible("input[id='overdue']")
        self.page.click("input[id='overdue']")

    def select_min_sum_credit(self):
        self.page.is_visible("input[id='min_amount']")
        self.page.fill("input[id='min_amount']", min_sum_credit)

    def click_button_search(self):
        self.page.is_visible("button[class='btn btn-danger me-md-2']")
        self.page.click("button[class='btn btn-danger me-md-2']")