from overrides import overrides

from pages.product_page import ProductPage

class GiftCardPage(ProductPage):
    def __init__(self, page):
        super().__init__(page)
        self.recipient_name = page.locator("#giftcard_2_RecipientName")
        self.recipient_email = page.locator("#giftcard_2_RecipientEmail")
        self.sender_name = page.locator("#giftcard_2_SenderName")
        self.sender_email = page.locator("#giftcard_2_SenderEmail")
        self.message = page.locator("#giftcard_2_Message")
    
    def fill_recipient_name(self, input):
        self.recipient_name.fill(input)
    
    def fill_recipient_email(self, input):
        self.recipient_email.fill(input)
    
    def fill_sender_name(self, input):
        self.sender_name.fill(input)
    
    def fill_sender_email(self, input):
        self.sender_email.fill(input)
    
    def fill_message(self, input):
        self.message.fill(input)

    @overrides
    def select_configuration(self, product: dict) -> None:
        self.fill_recipient_name(product["recipient_name"])
        self.fill_recipient_email(product["recipient_email"])
        self.fill_sender_name(product["sender_name"])
        self.fill_sender_email(product["sender_email"])
        self.fill_message(product["message"])
        self.fill_product_quantity(product["qty"])
        self.click_add_to_cart_button()