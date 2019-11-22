# Implement a class to hold room information. This should have name and
# description attributes.
from item import Inventory


class Room:
    """Room information and available paths"""

    # Movement map
    directions = {
        'n': 'n_to',
        's': 's_to',
        'e': 'e_to',
        'w': 'w_to'
    }

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

    def get_available_paths(self):
        # Available paths based on selected room
        available_paths = {k: v for (k, v) in self.directions.items(
        ) if getattr(self, v) != None}

        return available_paths

    def display_available_paths(self):
        print(f'Your available paths are:')
        for k, v in self.get_available_paths().items():
            print(f'{k.upper()}: {getattr(self, v).name}')
