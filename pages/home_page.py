from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.HOME_PAGE_URL = "https://demowebshop.tricentis.com/"       # Constant url for homepage
        self._items = page.locator(".item-box")                         # Represents locator for items on the homepage
    
    @property
    def items(self):
        """
        Read‑only property exposing the locator for all product item boxes.
        """
        return self._items
    
    def click_on_home_page_product(self, product_name: str) -> None:
        """
        Loops through each item box on the homepage, finds the one whose
        text contains `product_name`, and clicks its details link.

        Raises:
            ValueError: if no matching product is found.
        """
        total_items = self.items.count()

        for idx in range(total_items):
            item_box = self.items.nth(idx)
            # Retrieve the full text inside this item box
            text = item_box.inner_text()
            # If our desired product name appears in that text, click it
            if product_name in text:
                item_box.locator(".details a").click()
                return

        # If we exit the loop without returning, the product wasn't found
        raise ValueError(f"Product '{product_name}' not found on the homepage.")
