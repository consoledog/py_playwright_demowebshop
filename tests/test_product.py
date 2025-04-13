import pytest
import logging
import allure
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.gift_cart_page import GiftCardPage
from pages.comp_radio_page import CompRadioPage
from pages.comp_drop_page import CompDropDownPage

logger = logging.getLogger(__name__)

# Example list of product combinations to test
all_combinations = [
    # Combination 1
    [
        {
            "name": "Build your own computer",
            "config": "computer_drop_down_processor_ram",
            "qty": "1",
            "processor": "2.2 GHz Intel Pentium Dual-Core E2200",
            "ram": "2 GB",
            "hdd": "400 GB",
            "os": "Windows 7",
            "software": ["Acrobat Reader"],
        },
        {
            "name": "$25 Virtual Gift Card",
            "config": "gift_card_config",
            "qty": "1",
            "recipient_name": "Alex",
            "recipient_email": "alex@gmail.com",
            "sender_name": "Nenad",
            "sender_email": "nenad@gmail.com",
            "message": "This is your gift card. Happy birthday",
        },
        {
            "name": "Simple Computer",
            "config": "computer_radio_button_processor_ram",
            "qty": "1",
            "processor": "Slow",
            "ram": "8 GB",
            "hdd": "400 GB",
            "software": ["Image Viewer", "Office Suite"],
        },
        {
            "name": "14.1-inch Laptop",
            "config": "no_config",
            "qty": "1"
        }
    ]
]

@allure.feature("Product Search")
@allure.story("Search with different product combinations")
@pytest.mark.parametrize("combination", all_combinations)
def test_product_search(browser, combination):
    
    logger.info(f"Starting test for products: ")
    for product in combination:
        logger.info(product["name"])
    
    homepage = HomePage(browser)

    # 1) Go to the homepage
    homepage.navigate(homepage.HOME_PAGE_URL)

    # 2) In loop
    for product in combination:
        # 2.1) Open i-th item
        homepage.click_on_home_page_product(product["name"])
        # 2.2) Read and save i-th item information
        # 2.3) Select i-th item configuration and add the item to the cart
        product_item = None
        if   (product["config"] == "no_config"): product_item = ProductPage(browser)
        elif (product["config"] == "gift_card_config"): product_item = GiftCardPage(browser)
        elif (product["config"] == "computer_radio_button_processor_ram"): product_item = CompRadioPage(browser)
        elif (product["config"] == "computer_drop_down_processor_ram"): product_item = CompDropDownPage(browser)
        else:
            logger.error(f"Error in parameters: No such config")
        
        product_item.select_configuration(product)

        browser.pause()
        homepage.navigate(homepage.HOME_PAGE_URL)

    # 3) Go to the cart
    # 4) Check that correct 3 items are added in the cart
    # 5) Remove one item from the cart and verify it is removed
    # 6) Clear the cart
    # 7) Verify the cart is empty

