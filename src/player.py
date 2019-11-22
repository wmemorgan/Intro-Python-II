# Write a class to hold player information, e.g. what room they are in
# currently.
from inventory import Inventory


class Player:
    """Player characteristics, location, actions"""

    def __init__(self, name, current_room, inventory=Inventory('Player Inventory')):
        self.name = name
        self.current_room = current_room
        self.directions = self.current_room.directions # Reference Room class attributes
        self.inventory = inventory

    def __str__(self):
        output = f'{self.name}, located in {self.current_room.name},'

        if len(self.inventory.items) > 0:
            output += f" carries the following items:\n"
            output += self.inventory.display_inventory()

        return output

    def change_room(self, direction):
        self.current_room = getattr(self.current_room, self.directions[direction])
        print(f"You have entered the {self.current_room}")

    def get_item(self, item):
        self.inventory.add_item(item)
        self.current_room.inventory.remove_item(item)

    def drop_item(self, item):
        self.inventory.remove_item(item)
        self.current_room.inventory.add_item(item)
