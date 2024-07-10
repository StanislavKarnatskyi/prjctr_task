class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish: str, quantity: int):
        if dish in menu.keys():
            if (menu[dish]['quantity'] - quantity) >= 0:
                menu[dish]['quantity'] = menu[dish]['quantity'] - quantity
                print(f'{menu[dish]['price'] * quantity}$')
            else:
                print('Requested quantity not available')
        else:
            print("Dish not available")


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}
