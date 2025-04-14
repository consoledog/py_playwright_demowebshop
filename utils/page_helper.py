from playwright.sync_api import Locator
# These are the functions that are common for more than one page

def select_item(li_items: Locator, selection: str) -> None:

    """
    Iterate through a list of <li> elements containing radio buttons,
    find the one whose label text includes the given selection string,
    and check its associated radio input.

    Args:
        li_items (Locator): Locator for the collection of <li> elements.
        selection (str): Substring to match against each <li>'s <label> text.
    """
        
    count = li_items.count()

    for index in range(count):
        current_li = li_items.nth(index)
        label_text = current_li.locator("label").inner_text()
        if selection in label_text:
            # Found the matching label
            current_li.locator("input[type=radio]").check()
            break

def select_software(software_locator: Locator, selection: str) -> None:
    """
    Iterate through a list of <li> elements containing checkboxes,
    find the one whose label text includes the given selection string,
    and check its associated checkbox input.

    Args:
        software_locator (Locator): Locator for the parent element (For example <ul>) 
            that contains multiple <li> items, each with a <label> and checkbox.
        selection (str): Substring to match against each <label> text.
    """
        
    li_items = software_locator.locator("li")
    count = li_items.count()

    for index in range(count):
        current_li = li_items.nth(index)
        label_text = current_li.locator("label").inner_text()
        if selection in label_text:
            # Found the matching label
            current_li.locator("input[type=checkbox]").check()
            break