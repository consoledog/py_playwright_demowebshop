from overrides import overrides
from pages.product_page import ProductPage
import utils.page_helper as pageHelper

class CompDropDownPage(ProductPage):
    def __init__(self, page):
        super().__init__(page)
        self.processor = page.locator("select").nth(0)
        self.ram = page.locator("//select[@id='product_attribute_16_6_5']")
        self.hdd = page.locator("ul.option-list").nth(0)
        self.os = page.locator("ul.option-list").nth(1)
        self.software = page.locator("ul.option-list").nth(2)
    
    def select_processor(self, procesor_label: str) -> None:
        """
        Selects the processor from dropdown menu using label
        """
        self.processor.wait_for(state="visible", timeout=30000)
        self.processor.select_option(label = procesor_label)
    
    def select_ram(self, ram_label: str) -> None:
        """
        Selects the RAM value from dropdown menu using label
        """
        self.ram.wait_for(state="visible", timeout=30000)
        self.ram.select_option(label = ram_label)
    
    def select_hdd(self, selection: str) -> None:
        li_items = self.hdd.locator("li")
        pageHelper.select_item(li_items, selection)

    def select_os(self, selection: str) -> None:
        li_items = self.os.locator("li")
        pageHelper.select_item(li_items, selection)
    
    @overrides
    def select_configuration(self, product: dict) -> None:
        self.select_processor(product["processor"])
        self.select_ram(product["ram"])
        self.select_hdd(product["hdd"])
        self.select_os(product["os"])
        for software in product["software"]:
            pageHelper.select_software(self.software, software)
        self.fill_product_quantity(product["qty"])
        self.click_add_to_cart_button()