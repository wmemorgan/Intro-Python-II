# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Inventory


class Player:
    """Player characteristics, location, actions"""

    def __init__(self, name, current_room, inventory=Inventory('Player Inventory')):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        output = f'{self.name}, located in {self.current_room.name},'

        if len(self.inventory.items) > 0:
            output += f" carries the following items:\n"
            output += self.inventory.display_inventory()

        return output

    def change_room(self, room):
        self.current_room = getattr(self.current_room, room)
        print(f"You have entered the {self.current_room}\n")
