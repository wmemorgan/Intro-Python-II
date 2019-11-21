# Implement a class to hold room information. This should have name and
# description attributes.
from item import Inventory


class Room:
    """Room information and available paths"""

    def __init__(self, name, description, inventory=Inventory('Room Inventory')):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        output = f'{self.name}'

        if len(self.inventory.items) > 0:
            output += f" which contains: \n"
            output += self.inventory.display_inventory()
        else:
            output += f"\n"

        return output
