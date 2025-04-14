from overrides import overrides
import utils.page_helper as page_helper
from pages.product_page import ProductPage

class CompRadioPage(ProductPage):
    def __init__(self, page):
        super().__init__(page)
        self._processor = page.locator("ul.option-list").nth(0)     # Represents locator for selecting a processor type
        self._ram = page.locator("ul.option-list").nth(1)           # Represents locator for selecting RAM
        self._hdd = page.locator("ul.option-list").nth(2)           # Represents locator for selecting HDD config
        self._software = page.locator("ul.option-list").nth(3)      # Represents locator for selecting softwares
    
    @property
    def processor(self):
        """Read-only property exposing the processor options list locator."""
        return self._processor

    @property
    def ram(self):
        """Read-only property exposing the RAM options list locator."""
        return self._ram

    @property
    def hdd(self):
        """Read-only property exposing the HDD options list locator."""
        return self._hdd

    @property
    def software(self):
        """Read-only property exposing the software options list locator."""
        return self._software

    def _select_processor(self, selection: str) -> None:
        """
        Selects the processor option from the processor list that matches the given selection text.
        
        Parameters:
          selection (str): The visible text of the processor option to select.
        """
        # Retrieve the list items (li elements) within the processor locator
        li_items = self.processor.locator("li")
        # Use a helper function to select the desired item
        page_helper.select_item(li_items, selection)

    def _select_ram(self, selection: str) -> None:
        """
        Selects the RAM option from the RAM list that matches the given selection text.
        
        Parameters:
          selection (str): The visible text of the RAM option to select.
        """
        li_items = self.ram.locator("li")
        page_helper.select_item(li_items, selection)
    
    def _select_hdd(self, selection: str) -> None:
        """
        Selects the HDD option from the HDD list that matches the given selection text.
        
        Parameters:
          selection (str): The visible text of the HDD option to select.
        """
        li_items = self.hdd.locator("li")
        page_helper.select_item(li_items, selection)
    
    @overrides
    def select_configuration(self, product: dict) -> None:
        """
        Selects the complete configuration for the product by:
        - Selecting the processor, RAM, and HDD options.
        - Iterating over the software list and selecting each software option.
        - Filling in the quantity.
        - Clicking the 'Add to Cart' button.
        
        Parameters:
          product (dict): A dictionary containing product configuration details, etc:
            {
                "processor": "Slow",
                "ram": "8 GB",
                "hdd": "400 GB",
                "software": ["Image Viewer", "Office Suite"],
                "qty": "1"
            }
        """
        self._select_processor(product["processor"])
        self._select_ram(product["ram"])
        self._select_hdd(product["hdd"])
        for software in product["software"]:
            page_helper.select_software(self.software, software)
        self._fill_product_quantity(product["qty"])
        self._click_add_to_cart_button()