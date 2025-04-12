from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = "input[name='q']"
        self.search_button = "button[type='submit']"

    def search_product(self, product: str):
        self.page.fill(self.search_input, product)
        self.page.click(self.search_button)
