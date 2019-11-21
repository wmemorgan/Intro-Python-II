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


class Inventory:
    """Inventory management"""

    def __init__(self, name, items=[]):
        self.name = name
        self.items = items

    def __str__(self):
        return f"{self.name} number of items: {len(self.items)}"

    def display_inventory(self):
        if len(self.items) > 0:
            size = max(len(str(word)) for word in self.items)
            padding = 4
            indent = 2
            output = '\n' + ' ' * (indent) + '*' * (size + padding) + '\n'
            for word in self.items:
                output += ' ' * (indent) + \
                    '* {a:<{b}} *\n'.format(a=str(word), b=size)
            output += ' ' * (indent) + '*' * (size + padding) + '\n'
        else:
            output = f'no items available'

        return output

    def add_item(self, item):
        self.items.append(item)
        print(f'Added {item}\n')

    def remove_item(self, item):
        self.items.remove(item)
        print(f'Dropped {item}\n')
