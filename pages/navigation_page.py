from pages.base_page import BasePage

class NavigationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._shopping_cart_locator = page.locator("span.cart-label:has-text('Shopping cart')")     # Shopping cart locator button

    @property
    def shopping_cart(self):
        """
        Read‑only property exposing the locator for the 'Shopping cart' link in the navigation.
        """
        return self._shopping_cart_locator

    def click_on_shopping_cart(self) -> None:
        """
        Clicks on the 'Shopping cart' link in the site navigation.

        Raises:
            RuntimeError: if the shopping cart locator is not visible or clickable.
        """
        self.shopping_cart.wait_for(state="visible", timeout=5000)
        try:
            self.shopping_cart.click()
        except Exception as e:
            raise RuntimeError("Failed to click on the Shopping cart link") from e
