from typing import List
from typing import Optional
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

    def click_on_update_shopping_cart(self) -> None:
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

    def are_products_quantity_match(self, products: list[dict]) -> bool:
        """
        Checks that for each expected product in 'products', a cart item with the same product name exists
        and the quantity matches.
        """
        for expected_product in products:
            expected_name = expected_product["name"].strip()
            expected_qty  = expected_product["qty"].strip()  # expected quantity as a string

            # Flag to indicate if we found the product in the cart
            found = False
            
            for item in self.item_list:
                actual_name = item.productName.text_content().strip()
                if actual_name == expected_name:
                    found = True
                    actual_qty = item.get_quantity_value().strip()
                    if actual_qty != expected_qty:
                        self.logger.error(
                            f"Quantity mismatch for product '{expected_name}': expected {expected_qty}, got {actual_qty}"
                        )
                        return False
                    # Found matching product and quantity, so break out of inner loop
                    break
            
            # If we didn't find the expected product in the cart, return False
            if not found:
                self.logger.error(f"Product '{expected_name}' not found in the cart.")
                return False
        return True

    def remove_item_from_cart(self, item_name: str) -> Optional[str]:
        """
        Finds the cart item with the matching product name,
        ticks its removal checkbox, updates, and returns the item's id.
        """
        removed_id = None
        found = False

        for item in self.item_list:
            if item.productName.text_content().strip() == item_name:
                found = True
                removed_id = item.id
                item.select_item_to_remove()
                self.logger.info(f"Marked item '{item_name}' for removal.")
                break
        
        if not found:
            self.logger.error(f"Item '{item_name}' not found in the cart.")
            return None

        # Click the update button
        self.click_on_update_shopping_cart()
        self.logger.info(f"Removed item '{item_name}' from the cart.")

        # Re-scan the cart so self.item_list matches the new page state
        self.item_list.clear()
        self.init_item_list()

        return removed_id
    
    def is_item_cart_removed(self, item_id: str) -> bool:

        for item in self.item_list:
            if item.id == item_id:
                return False
        return True
    
    def clear_cart(self) -> None:
        # Mark all items for removal
        for item in self.item_list:
            item.select_item_to_remove()

        # After marking all checkboxes, remove them from the cart
        self.click_on_update_shopping_cart()
        
        # Clear the list
        self.item_list.clear()
        self.logger.info("Cart has been cleared.")
    
    def is_cart_clear(self) -> bool:
        return len(self.item_list) == 0