class Item:
    """Item information"""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'


class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories


class Gold(Item):
    """CRUD functionality for gold item"""

    def __init__(self, quantity=0):
        super().__init__('Gold', 'Use it to buy items')
        self.quantity = quantity

    def __str__(self):
        return f'{self.quantity} {self.name.lower()} coins'

    def increase(self, quantity):
        if quantity > 0:
            self.quantity += quantity
            print(
                f'Added {quantity} gold coin(s). You have {self.quantity} coin(s).')
        else:
            print('Invalid value')

    def decrease(self, quantity):
        if quantity > 0:
            if quantity > self.quantity:
                return 'Insufficient amount'
            else:
                self.quantity -= quantity

        else:
            print('Invalid value')
