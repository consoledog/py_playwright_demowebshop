# Example list - List of 3 different products
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

# Assign simple numeric IDs based on the index of each combination.
# On this way the test knows itself what combinations is currently tested, so can do indexing like all_combinations[combination_index]
combination_ids = list(range(len(all_combinations)))  # e.g. [0, 1, 2, ...]