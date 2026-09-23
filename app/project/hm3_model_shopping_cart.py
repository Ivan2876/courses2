class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name: str, price: float, quantity: int):
        for item in self.items:
            if item['name'] == name:
                item['quantity'] += quantity
                item['price'] = price
                return

        new_item = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        self.items.append(new_item)

    def remove_item(self, name: str):
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)

    def get_summa(self) -> int:
        summa = sum(item['price'] * item['quantity'] for item in self.items)
        print(f"Total value of items in your cart {summa} grn")
        return summa