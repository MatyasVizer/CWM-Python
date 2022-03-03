# property is an object that sits in front of an attribute
# and allows as to get or set the value of the attribute


class Product:
    def __init__(self, price):
        self.price = price

    @property  # it will automatically create a property object
    def price(self):
        return self.__price

    @price.setter  # starts with the name of property ob-ject
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative.")
        self.__price = value


product = Product(10)
print(product.price)
