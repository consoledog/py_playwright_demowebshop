from overrides import overrides
from pages.product_page import ProductPage
import utils.page_helper as page_helper

class CompDropDownPage(ProductPage):
    def __init__(self, page):
        super().__init__(page)
        self._processor = page.locator("select").nth(0)                         # Represents locator for selecting a processor type
        self._ram = page.locator("//select[@id='product_attribute_16_6_5']")    # Represents locator for selecting RAM
        self._hdd = page.locator("ul.option-list").nth(0)                       # Represents locator for selecting HDD config
        self._os = page.locator("ul.option-list").nth(1)                        # Represents locator for selecting operating systems
        self._software = page.locator("ul.option-list").nth(2)                  # Represents locator for selecting softwares
    
    @property
    def processor(self):
        """Read-only locator for the processor dropdown."""
        return self._processor

    @property
    def ram(self):
        """Read-only locator for the RAM dropdown."""
        return self._ram

    @property
    def hdd(self):
        """Read-only locator for the HDD option list."""
        return self._hdd

    @property
    def os(self):
        """Read-only locator for the OS option list."""
        return self._os

    @property
    def software(self):
        """Read-only locator for the software option list."""
        return self._software

    def _select_processor(self, processor_label: str) -> None:
        """
        Selects the processor from the dropdown menu using the given label.
        """
        self.processor.wait_for(state="visible", timeout=30000)
        self.processor.select_option(label=processor_label)
    
    def _select_ram(self, ram_label: str) -> None:
        """
        Selects the RAM value from the dropdown menu using the given label.
        """
        self.ram.wait_for(state="visible", timeout=30000)
        self.ram.select_option(label=ram_label)
    
    def _select_hdd(self, selection: str) -> None:
        """
        Selects the HDD option from the option list.
        """
        li_items = self.hdd.locator("li")
        page_helper.select_item(li_items, selection)

    def _select_os(self, selection: str) -> None:
        """
        Selects the OS option from the option list.
        """
        li_items = self.os.locator("li")
        page_helper.select_item(li_items, selection)
    
    @overrides
    def select_configuration(self, product: dict) -> None:
        """
        Selects the full configuration for a computer product:
        processor, RAM, HDD, OS, additional software, quantity,
        and finally adds the product to the cart.
        """
        self._select_processor(product["processor"])
        self._select_ram(product["ram"])
        self._select_hdd(product["hdd"])
        self._select_os(product["os"])
        for software in product["software"]:
            page_helper.select_software(self.software, software)
        self._fill_product_quantity(product["qty"])
        self._click_add_to_cart_button()
