from overrides import overrides
from pages.product_page import ProductPage

class GiftCardPage(ProductPage):
    def __init__(self, page):
        super().__init__(page)
        # Initialize locators as private attributes to make them read-only
        self._recipient_name = page.locator("#giftcard_2_RecipientName")        # Locator for recipient name field
        self._recipient_email = page.locator("#giftcard_2_RecipientEmail")      # Locator for recipient emil field
        self._sender_name = page.locator("#giftcard_2_SenderName")              # Locator for sender name field
        self._sender_email = page.locator("#giftcard_2_SenderEmail")            # Locator for sender email field
        self._message = page.locator("#giftcard_2_Message")                     # Locator for message field

    # Read-only properties to expose the locators
    @property
    def recipient_name(self):
        """Read-only locator for the recipient name input."""
        return self._recipient_name

    @property
    def recipient_email(self):
        """Read-only locator for the recipient email input."""
        return self._recipient_email

    @property
    def sender_name(self):
        """Read-only locator for the sender name input."""
        return self._sender_name

    @property
    def sender_email(self):
        """Read-only locator for the sender email input."""
        return self._sender_email

    @property
    def message(self):
        """Read-only locator for the gift card message input."""
        return self._message

    # private, and public methods to fill in individual fields using the read-only properties

    def _fill_recipient_name(self, value: str) -> None:
        """Fills the recipient name field with the provided value."""
        self.recipient_name.fill(value)
    
    def _fill_recipient_email(self, value: str) -> None:
        """Fills the recipient email field with the provided value."""
        self.recipient_email.fill(value)
    
    def _fill_sender_name(self, value: str) -> None:
        """Fills the sender name field with the provided value."""
        self.sender_name.fill(value)
    
    def _fill_sender_email(self, value: str) -> None:
        """Fills the sender email field with the provided value."""
        self.sender_email.fill(value)
    
    def _fill_message(self, value: str) -> None:
        """Fills the message field with the provided value."""
        self.message.fill(value)

    @overrides
    def select_configuration(self, product: dict) -> None:
        """
        Configures the gift card page using the product dictionary.
        Calls methods to fill in recipient/sender details and message,
        then fills the quantity and clicks the add-to-cart button.
        """
        self._fill_recipient_name(product["recipient_name"])
        self._fill_recipient_email(product["recipient_email"])
        self._fill_sender_name(product["sender_name"])
        self._fill_sender_email(product["sender_email"])
        self._fill_message(product["message"])
        self._fill_product_quantity(product["qty"])
        self._click_add_to_cart_button()
