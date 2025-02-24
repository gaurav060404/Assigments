class Purchase:
    list_of_items = ['Cake', 'Soap', 'Jam', 'Cereal', 'Hand Sanitizer', 'Biscuits', 'Bread']
    list_of_count_of_each_item_sold = [0] * len(list_of_items)

    def __init__(self):   
        self.items_purchased = [] 
        self.item_on_offer = None  

    def sell_items(self, items_to_be_purchased):
        for item in items_to_be_purchased:
            if item in Purchase.list_of_items:
                index = Purchase.list_of_items.index(item)
                Purchase.list_of_count_of_each_item_sold[index] += 1
                self.items_purchased.append(item)
        if "Soap" in items_to_be_purchased: 
            self.provide_offer()

    def provide_offer(self):
        sanitizer_index = Purchase.list_of_items.index("Hand Sanitizer")
        Purchase.list_of_count_of_each_item_sold[sanitizer_index] += 1
        self.item_on_offer = "Hand Sanitizer"
        self.items_purchased.append("Hand Sanitizer")

    def get_items_purchased(self):
        return self.items_purchased

    def get_item_on_offer(self):
        return self.item_on_offer

customer1 = Purchase()
customer1.sell_items(["Soap", "Cake"])
print("Items Purchased:", customer1.get_items_purchased())
print("Item on Offer:", customer1.get_item_on_offer())