import pytest
import logging
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.gift_cart_page import GiftCardPage
from pages.comp_radio_page import CompRadioPage
from pages.comp_drop_page import CompDropDownPage
from pages.navigation_page import NavigationPage
from pages.shoping_cart_page import ShoppingCartPage

logger = logging.getLogger(__name__)

# Example list of product combinations to test
all_combinations = [
    # Combination 1
    [
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

# Assign unique IDs based on the index or some property of the combination.
combination_ids = list(range(len(all_combinations)))  # [0, 1, 2, ...]

@pytest.mark.parametrize("combination", all_combinations, ids=combination_ids)
def test_product_add_remove(browser, combination, request):
    
    combination_index = int(request.node.callspec.id.split('-')[-1])
    logger.info(f"Starting {combination_index} test data for products: ")
    for product in combination:
        logger.info(product["name"])
    
    homepage = HomePage(browser)

    logger.info("# 1) Go to the homepage")
    homepage.navigate(homepage.HOME_PAGE_URL)

    # 2) In loop
    for product in combination:

        logger.info(f"# 2.1) Open {product["name"]} item")
        homepage.click_on_home_page_product(product["name"])

        logger.info(f"# 2.2) Select {product["name"]} item configuration and add the item to the cart")
        # Note: Code below is for selecting the configuration of a product (Like selecting type of processor, RAM, etc.)
        product_item = None
        if   (product["config"] == "no_config"): product_item = ProductPage(browser)
        elif (product["config"] == "gift_card_config"): product_item = GiftCardPage(browser)
        elif (product["config"] == "computer_radio_button_processor_ram"): product_item = CompRadioPage(browser)
        elif (product["config"] == "computer_drop_down_processor_ram"): product_item = CompDropDownPage(browser)
        else:
            logger.error(f"Error in parameters: No such config")
        
        product_item.select_configuration(product)
        homepage.navigate(homepage.HOME_PAGE_URL)

    logger.info("# 3) Go to the cart")
    navigationPage = NavigationPage(browser)
    navigationPage.click_on_shopping_cart()
    
    logger.info("# 4) Check that correct items are added in the cart")
    shoppingCartPage = ShoppingCartPage(browser)
    assert shoppingCartPage.are_products_name_match(all_combinations[combination_index]), "Some products are missing in the shopping cart."
    assert shoppingCartPage.are_products_quantity_match(all_combinations[combination_index]), "Some quantities are not the same"
    
    logger.info(f"# 5) Remove item from the cart")
    item_id = shoppingCartPage.remove_item_from_cart(all_combinations[combination_index][1]["name"])

    logger.info(f"# 6) Verify item is removed")
    assert shoppingCartPage.is_item_cart_removed(item_id), f"Item with id {item_id} is still in the cart."
    
    logger.info("# 7) Clear the cart")
    shoppingCartPage.clear_cart()

    logger.info("# 8) Verify the cart is empty")
    assert shoppingCartPage.is_cart_clear(), f"Item cart is not empty"

