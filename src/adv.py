import re
from room import Room
from player import Player
from inventory import Inventory
from item import Item
from item import Gold
from item import Food

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Inventory('Room Inventory', [Item('cloak', 'wool cloak')])),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Inventory('Room Inventory', [Gold(1000)])),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# player = Player('George', room['outside'], Inventory(
#     'Player Inventory', [Gold(10), Food('apple', 'red delicious', 5)]))
player = Player('Harry', room['outside'], Inventory('Player Inventory', [Item(
    'Magic Wand', 'used for casting spells'), Item('Broom', 'used for transportation and sport')]))
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# REPL (Read, evaluate, print, loop)
main_menu = {
    'm': 'Menu',
    'i': 'Inventory Menu',
    'd': 'Available direction(s) ',
    'q': 'Quit the game',
}

def display_menu(menu):
    for k, v in menu.items():
        print(f"{k.upper()}: {v}")
    print("\n")

selection = ''
padding = len("located in, carries the following items:") + 4
top_border = f"{'=' * (int(len(player.name+player.current_room.name)+padding))}"
print(top_border)
print(player)
print(f'{player.current_room.description}\n')
display_menu(main_menu)
player.current_room.show_available_directions()
# LOOP
while selection != 'q':
    # READ
    selection = input("Choose a selection or press 'm' for the main menu: ").lower().strip()
    print(f"ROOM ITEMS: {[str(item) for item in player.current_room.inventory.items]}")
    # EVALUATE
    if selection == 'q':
        print('Thank you for playing!')
    elif selection == 'm':
        display_menu(main_menu)
    elif selection == 'd':
        player.current_room.show_available_directions()
    elif selection == 'i':
        display_menu(player.inventory.menu)
        inv_selection = ''

        while inv_selection != 'm':
            inv_selection = input(
                "Choose from the inventory menu or press 'm' to return to the main menu: ").lower().strip()

            if inv_selection == 'm':
                display_menu(main_menu)
            elif inv_selection == 'i':
                display_menu(player.inventory.menu)
            elif inv_selection == 'p':
                if (len(player.inventory.items) > 0):
                    print("You are carrying the following items:")
                print(player.inventory.show_inventory())

                item_selection = ''

                while item_selection != 'b':
                    item_selection = input("GET or DROP an item or press 'b' to return to the previous menu: ").lower().strip()
                    item_selection = re.sub(" +", " ", item_selection)
                    if item_selection == 'b':
                        print('Return to previous menu')
                    elif item_selection[:3] == 'get':
                        player.get_item(item_selection[3:].strip())
                    elif item_selection[:4] == 'drop':
                        player.drop_item(item_selection[4:].strip())
                
            elif inv_selection == 'r':
                if (len(player.current_room.inventory.items) > 0):
                    print(f"{player.current_room.name} contains:")
                print(player.current_room.inventory.show_inventory())

    elif selection not in player.current_room.get_available_directions():
        print('Error, please enter valid direction:\n')
    else:
        player.change_room(selection)
        player.current_room.show_available_directions()

bottom_border = f"\n{'=' * (int(len(player.current_room.description)))}\n"
print(bottom_border)
