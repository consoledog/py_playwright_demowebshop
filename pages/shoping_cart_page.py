from typing import List
from typing import Optional
import logging

from pages.base_page import BasePage
from pages.shoping_cart_item_page import ShoppingCartItemPage

class ShoppingCartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = logging.getLogger(__name__)                                           # Logger for the module
        self.update_shopping_cart = page.locator("input[value='Update shopping cart']")     # Locator for "Update shopping cart" button
        self.item_list: List[ShoppingCartItemPage] = []                                     # Locator for items in teh cart
        self.init_item_list()

    def init_item_list(self) -> None:
        """
        Scans the cart table for rows and builds ShoppingCartItemPage objects.
        """
        cart_rows = self.page.locator("tr.cart-item-row")
        row_count = cart_rows.count()

        for i in range(row_count):
            row = cart_rows.nth(i)
            # Find the removal checkbox, product name link, configuration text, and quantity input
            isSelectedToRemove = row.locator("input[name='removefromcart']")
            product_name       = row.locator("td.product a.product-name")
            configuration      = row.locator("div.attributes")
            quantity           = row.locator("input.qty-input")
            
            # Create and fill a ShoppingCartItemPage for this row
            item = ShoppingCartItemPage(self.page)
            item.fill_shoping_cart_item(
                isSelectedToRemove,
                product_name,
                configuration,
                quantity
            )
            self.item_list.append(item)

    def click_on_update_shopping_cart(self) -> None:
        """
        Clicks the 'Update shopping cart' button to apply any removals or quantity changes.
        """
        self.update_shopping_cart.click()

    def print_shoping_cart_items(self) -> None:
        """
        Logs each product name currently in the cart.
        """
        for item in self.item_list:
            product_text = item.product_name.text_content()
            self.logger.info(product_text)

    def are_products_name_match(self, products: List[dict]) -> bool:
        """
        Verifies that each expected product name appears in the cart.
        
        Args:
            products: List of dicts, each containing at least a "name" key.
        
        Returns:
            True if all expected names are found; False otherwise.
        """
        # Build a list of the actual names in the cart
        actual_names = [item.product_name.text_content().strip() for item in self.item_list]
        self.logger.info(f"Cart product names: {actual_names}")

        # Check presence of each expected name
        for product in products:
            expected = product["name"]
            if expected not in actual_names:
                self.logger.error(f"Product '{expected}' not found in the cart.")
                return False

        return True

    def are_products_quantity_match(self, products: List[dict]) -> bool:
        """
        For each expected product, finds its cart row and verifies the quantity matches.
        
        Args:
            products: List of dicts, each with "name" and "qty" keys.
        
        Returns:
            True if all quantities match; False otherwise.
        """
        for expected in products:
            name = expected["name"].strip()
            qty  = expected["qty"].strip()
            found = False

            for item in self.item_list:
                actual_name = item.product_name.text_content().strip()
                if actual_name == name:
                    found = True
                    actual_qty = item.get_quantity_value().strip()
                    if actual_qty != qty:
                        self.logger.error(
                            f"Quantity mismatch for '{name}': expected {qty}, got {actual_qty}"
                        )
                        return False
                    break  # quantity matched, move to next product

            if not found:
                self.logger.error(f"Product '{name}' not found in the cart.")
                return False

        return True

    def remove_item_from_cart(self, item_name: str) -> Optional[str]:
        """
        Checks the removal box for the given product, updates the cart,
        re-initializes item_list, and returns the removed item's id.
        
        Args:
            item_name: The exact product name to remove.
        
        Returns:
            The UUID of the removed ShoppingCartItemPage, or None if not found.
        """
        removed_id = None

        # Find and mark the item
        for item in self.item_list:
            if item.product_name.text_content().strip() == item_name:
                removed_id = item.id
                item.select_item_to_remove()
                self.logger.info(f"Marked '{item_name}' for removal.")
                break

        if removed_id is None:
            self.logger.error(f"Item '{item_name}' not found in the cart.")
            return None

        # Apply removal
        self.click_on_update_shopping_cart()
        self.logger.info(f"Removed '{item_name}' from the cart.")

        # Refresh our internal list to match the page
        self.item_list.clear()
        self.init_item_list()

        return removed_id

    def is_item_cart_removed(self, item_id: str) -> bool:
        """
        Checks whether an item with the given id is absent from the cart.
        
        Args:
            item_id: The UUID returned by remove_item_from_cart.
        
        Returns:
            True if the item is no longer in item_list; False otherwise.
        """
        for item in self.item_list:
            if item.id == item_id:
                return False
        return True

    def clear_cart(self) -> None:
        """
        Marks all items for removal and updates the cart, then clears the local list.
        """
        for item in self.item_list:
            item.select_item_to_remove()

        self.click_on_update_shopping_cart()
        
        # After removal, clear our internal representation
        self.item_list.clear()
        self.logger.info("Cart has been cleared.")

    def is_cart_clear(self) -> bool:
        """
        Returns True if there are no items left in the cart.
        """
        return len(self.item_list) == 0