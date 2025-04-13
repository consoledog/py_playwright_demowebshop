from pages.base_page import BasePage
from playwright.sync_api import Locator

class ShoppingCartItemPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.isSelected:    Locator = None          # Is the product selected to be removed from the cart
        self.productName:   Locator = None          # Represents the product name of the product in the cart
        self.configuration: Locator = None          # Represents the configuration of the product in the cart
        self.quantity:      Locator = None          # Represents the quantity of the product in the cart

    def fill_shoping_cart_item(self, 
                               isSelected:      Locator, 
                               productName:     Locator, 
                               configuration:   Locator,
                               quantity:        Locator) -> None:
        self.isSelected = isSelected
        self.productName = productName
        self.configuration = configuration
        self.quantity = quantity
    
    def select_item_to_remove(self) -> None:
        self.isSelected.check()
    
