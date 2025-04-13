from overrides import overrides
import utils.page_helper as pageHelper
from pages.product_page import ProductPage

class CompRadioPage(ProductPage):
    def __init__(self, page):
        super().__init__(page)
        self.processor = page.locator("ul.option-list").nth(0)
        self.ram = page.locator("ul.option-list").nth(1)
        self.hdd = page.locator("ul.option-list").nth(2)
        self.software = page.locator("ul.option-list").nth(3)

    def select_processor(self, selection: str) -> None:
        li_items = self.processor.locator("li")
        pageHelper.select_item(li_items, selection)

    def select_ram(self, selection: str) -> None:
        li_items = self.ram.locator("li")
        pageHelper.select_item(li_items, selection)
    
    def select_hdd(self, selection: str) -> None:
        li_items = self.hdd.locator("li")
        pageHelper.select_item(li_items, selection)
    
    @overrides
    def select_configuration(self, product: dict) -> None:
        self.select_processor(product["processor"])
        self.select_ram(product["ram"])
        self.select_hdd(product["hdd"])
        for software in product["software"]:
            pageHelper.select_software(self.software, software)
        self.fill_product_quantity(product["qty"])
        self.click_add_to_cart_button()