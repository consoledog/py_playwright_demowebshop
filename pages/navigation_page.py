from pages.base_page import BasePage

class NavigationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.shopping_cart = page.locator("span.cart-label:has-text('Shopping cart')")

    def search_product(self, product: str):
        self.page.fill(self.search_input, product)
        self.page.click(self.search_button)