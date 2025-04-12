from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.HOME_PAGE_URL = "https://demowebshop.tricentis.com/"
        self.items = page.locator(".item-box")
    
    def click_on_home_page_product(self, product_name: str):
        """
        Loops through the item boxes, finds the one containing product_name, 
        and clicks on it.
        """
        count = self.items.count()

        for index in range(count):
            item_box = self.items.nth(index)

            # Retrieve the text content of the current item
            text = item_box.inner_text()

            # If product_name matches the text then click on it
            if product_name in text:
                item_box.locator(".details a").click()
                break
