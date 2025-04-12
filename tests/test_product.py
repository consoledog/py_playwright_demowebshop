import pytest
import logging
import allure
from pages.home_page import HomePage

logger = logging.getLogger(__name__)

# Example list of product combinations to test
product_data = [
    ("laptop", "high-end"),
    ("smartphone", "budget"),
    ("headphones", "wireless")
]

@allure.feature("Product Search")
@allure.story("Search with different product combinations")
@pytest.mark.parametrize("product, variant", product_data)
def test_product_search(browser, product, variant):
    logger.info(f"Starting test for product: {product}, variant: {variant}")

    # 1) Go to the homepage
    # 2) In loop
        # 2.1) Open i-th item
        # 2.2) Read and save i-th item information
        # 2.3) If possible, select i-th item configuration
        # 2.4) Add i-th item to the cart
    # 3) Go to the cart
    # 4) Check that correct 3 items are added in the cart
    # 5) Remove one item from the cart and verify it is removed
    # 6) Clear the cart
    # 7) Verify the cart is empty

