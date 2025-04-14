from pages.base_page import BasePage
from playwright.sync_api import Locator
import uuid

class ShoppingCartItemPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Generate a stable unique identifier for this cart item instance
        self._id: str = str(uuid.uuid4())           # Id of the cart item
        
        # These will be set later via fill_shoping_cart_item; until then they remain None
        self._is_selected: Locator = None           # Is the product selected to be removed from the cart            
        self._product_name: Locator = None          # Represents the product name of the product in the cart
        self._configuration: Locator = None         # Represents the configuration of the product in the cart
        self._quantity: Locator = None              # Represents the quantity of the product in the cart

    @property
    def id(self) -> str:
        """
        Read‑only property returning this item's unique identifier.
        """
        return self._id

    @property
    def is_selected(self) -> Locator:
        """
        Read‑only property exposing the checkbox locator used to mark this item for removal.
        """
        return self._is_selected

    @property
    def product_name(self) -> Locator:
        """
        Read‑only property exposing the locator for this item's product name link.
        """
        return self._product_name

    @property
    def configuration(self) -> Locator:
        """
        Read‑only property exposing the locator for this item's configuration details.
        """
        return self._configuration

    @property
    def quantity(self) -> Locator:
        """
        Read‑only property exposing the locator for this item's quantity input.
        """
        return self._quantity

    def fill_shoping_cart_item(
        self,
        is_selected: Locator,
        product_name: Locator,
        configuration: Locator,
        quantity: Locator
    ) -> None:
        """
        Initializes this cart item with its relevant locators.
        
        Parameters:
          is_selected (Locator): checkbox to remove the item
          product_name (Locator): link or text element showing the product name
          configuration (Locator): element showing the chosen configuration
          quantity (Locator): input element for the quantity
        """
        self._is_selected = is_selected
        self._product_name = product_name
        self._configuration = configuration
        self._quantity = quantity

    def select_item_to_remove(self) -> None:
        """
        Checks the removal checkbox for this item.
        """
        self.is_selected.check()

    def get_quantity_value(self) -> str:
        """
        Returns the current 'value' attribute of the quantity input.
        """
        return self.quantity.input_value()
