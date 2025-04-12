from overrides import overrides
from playwright.sync_api import Locator

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
        self.select_item(li_items, selection)

    def select_ram(self, selection: str) -> None:
        li_items = self.ram.locator("li")
        self.select_item(li_items, selection)
    
    def select_hdd(self, selection: str) -> None:
        li_items = self.hdd.locator("li")
        self.select_item(li_items, selection)
    
    def select_software(self, selection: str) -> None:
        li_items = self.software.locator("li")
        count = li_items.count()

        for index in range(count):
            current_li = li_items.nth(index)
            label_text = current_li.locator("label").inner_text()
            if selection in label_text:
                # Found the matching label
                current_li.locator("input[type=checkbox]").check()
                break

    def select_item(self, li_items: Locator, selection: str) -> None:
        count = li_items.count()

        for index in range(count):
            current_li = li_items.nth(index)
            label_text = current_li.locator("label").inner_text()
            if selection in label_text:
                # Found the matching label
                current_li.locator("input[type=radio]").check()
                break
    
    @overrides
    def select_configuration(self, product: dict) -> None:
        self.select_processor(product["processor"])
        self.select_ram(product["ram"])
        self.select_hdd(product["hdd"])
        for software in product["software"]:
            self.select_software(software)
        self.fill_product_quantity(product["qty"])
        self.click_add_to_cart_button()