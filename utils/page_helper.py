from playwright.sync_api import Locator
# These are the functions that are common for more than one page

def select_item(li_items: Locator, selection: str) -> None:
    count = li_items.count()

    for index in range(count):
        current_li = li_items.nth(index)
        label_text = current_li.locator("label").inner_text()
        if selection in label_text:
            # Found the matching label
            current_li.locator("input[type=radio]").check()
            break

def select_software(software_locator: Locator, selection: str) -> None:
    li_items = software_locator.locator("li")
    count = li_items.count()

    for index in range(count):
        current_li = li_items.nth(index)
        label_text = current_li.locator("label").inner_text()
        if selection in label_text:
            # Found the matching label
            current_li.locator("input[type=checkbox]").check()
            break