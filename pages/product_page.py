from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.name               = page.locator("h1[itemprop='name']")                   # Locator used for name text of the product
        self.qty                = page.locator("input.qty-input")                       # Locator used for input field related to quantity
        self.add_to_cart_button = page.locator("input.button-1.add-to-cart-button")     # Locator used to get "Add to cart" button

    def _fill_product_quantity(self, input: str):
        """
        Fill the quantity of the product
        """
        self.qty.fill(input)
    
    def _click_add_to_cart_button(self):
        """
        Click button to add the product into the cart
        """
        self.add_to_cart_button.click()
    
    def select_configuration(self, product: dict) -> None:
        """
        Select the quantity and click "Add to Cart" button
        """
        self._fill_product_quantity(product["qty"])
        self._click_add_to_cart_button()