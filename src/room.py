# Implement a class to hold room information. This should have name and
# description attributes.
from inventory import Inventory
from design import Color

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
        output = f"{Color.CYAN}{Color.BOLD}{self.name}{Color.END}"

        if len(self.inventory.items) > 0:
            output += f" which contains: \n"
            output += self.inventory.show_inventory()
        else:
            output += f"\n"

        return output

    def get_available_directions(self):
        # Available paths based on selected room
        available_paths = {k: v for (k, v) in self.directions.items(
        ) if getattr(self, v) != None}

        return available_paths

    def show_available_directions(self):
        print(f'Your available paths are:')
        for k, v in self.get_available_directions().items():
            print(f'{Color.PURPLE}{k.upper()}: {getattr(self, v).name}{Color.END}')
