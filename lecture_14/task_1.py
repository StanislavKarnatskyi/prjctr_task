class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def __str__(self):
        return f'Name: {self.name}, author {self.author}. Quantity {self.quantity} and price {self.price}'

