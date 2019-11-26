from item import Item
from item import Gold
from design import Color

class Inventory:
    """Inventory management"""

    def __init__(self, name, items=[]):
        self.name = name
        self.items = items

    def __str__(self):
        return f"{self.name} number of items: {len(self.items)} {self.items}"

    def show_inventory(self):
        if len(self.items) > 0:
            size = max(len(str(word)) for word in self.items)
            padding = 4
            indent = 2
            output = '\n' + Color.YELLOW + ' ' * \
                (indent) + '*' * (size + padding) + '\n'
            for word in self.items:
                output += ' ' * (indent) + \
                    '* {a:<{b}} *\n'.format(a=str(word), b=size)
            output += ' ' * (indent) + '*' * (size + padding) + Color.END + '\n' 
        else:
            output = f"\n  {Color.RED}**NO ITEMS AVAILABLE**{Color.END}  \n"

        return output

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        old_item = [item for item in self.items if item.name == item_name][0]
        self.items = [item for item in self.items if item.name != item_name]
        return old_item
