from typing import List
import logging

from pages.base_page import BasePage
from pages.shoping_cart_item_page import ShoppingCartItemPage

class ShoppingCartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = logging.getLogger(__name__)
        self.update_shopping_cart = page.locator("input[value='Update shopping cart']")

        self.item_list: List[ShoppingCartItemPage] = []
        self.init_item_list()

    def init_item_list(self):
        cart_rows = self.page.locator("tr.cart-item-row")
        row_count = cart_rows.count()

        for i in range(row_count):
            row = cart_rows.nth(i)
            isSelectedToRemove = row.locator("input[name='removefromcart']")
            productName = row.locator("td.product a.product-name")
            configuration = row.locator("div.attributes")
            quantity = row.locator("input.qty-input")
            
            item = ShoppingCartItemPage(self.page)
            item.fill_shoping_cart_item(isSelectedToRemove, productName, configuration, quantity)
            self.item_list.append(item)

    def click_on_update_shoping_cart(self) -> None:
        self.update_shopping_cart.click()

    def print_shoping_cart_items(self) -> List:
        for item in self.item_list:
            # Using text_content() can sometimes avoid visibility issues.
            product_text = item.productName.text_content()
            self.logger.info(product_text)
    
    def are_products_name_match(self, products: list[dict]) -> bool:
        
        product_name_list = [item.productName.text_content().strip() for item in self.item_list]
        self.logger.info(f"Cart product names: {product_name_list}")

        # Check that every product's "name" (from the products list) is found in product_name_list
        for product in products:
            if product["name"] not in product_name_list:
                self.logger.error(f"Product '{product['name']}' not found in the cart.")
                return False
        
        return True


