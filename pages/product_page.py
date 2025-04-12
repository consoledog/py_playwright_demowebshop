from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.name               = page.locator("h1[itemprop='name']")
        self.qty                = page.locator("input.qty-input")
        self.add_to_cart_button = page.locator("input.button-1.add-to-cart-button")

    def read_product_name(self):
        return self.name.inner_text()

    def fill_product_quantity(self, input: str):
        self.qty.fill(input)
    
    def click_add_to_cart_button(self):
        self.add_to_cart_button.click()
    
    def select_configuration(self, product: dict) -> None:
        self.fill_product_quantity(product["qty"])
        self.click_add_to_cart_button()