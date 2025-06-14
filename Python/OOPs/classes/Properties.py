class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be Zero or Less")
        self.__price = value


product = Product(10)
product.price = 2
print(product.price)
