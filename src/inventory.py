class Inventory:
    """Inventory management"""
    menu = {
        'i': 'Inventory Menu',
        'p': 'Player inventory',
        'r': 'Room inventory',
        'm': 'Go back to main menu',
    }

    def __init__(self, name, items=[]):
        self.name = name
        self.items = items

    def __str__(self):
        return f"{self.name} number of items: {len(self.items)}"

    def show_inventory(self):
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
