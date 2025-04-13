from pages.base_page import BasePage

class NavigationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.shopping_cart = page.locator("span.cart-label:has-text('Shopping cart')")

    def click_on_shopping_cart(self) -> None:
        self.shopping_cart.click()