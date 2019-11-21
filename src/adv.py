from room import Room
from player import Player
from item import Inventory
from item import Item
from item import Gold
from item import Food

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

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
selection = ''
padding = 4
top_border = f"{'=' * (int(len(player.name+player.current_room.name)+padding))}"
print(top_border)
print(player)
# LOOP
while selection != 'q':
    print(f'{player.current_room.description}\n')
    # Valid movement
    directions = {
        'n': 'n_to',
        's': 's_to',
        'e': 'e_to',
        'w': 'w_to'
    }
    # Available paths based on current room
    available_paths = {k: v for (k, v) in directions.items(
    ) if getattr(player.current_room, v) != None}

    print(f'Your available paths are:')
    for k, v in available_paths.items():
        print(f'{k.upper()}: {getattr(player.current_room, v).name}')

    # READ
    selection = input(
        "\nChoose a direction or 'q' to quit the game : ").lower().strip()
    # EVALUATE
    if selection == 'q':
        print('Thank you for playing')
    elif selection not in available_paths:
        print('Error, please enter valid direction:\n')
    else:
        player.change_room(available_paths[selection])
        player.current_room.inventory.add_item(
            Item("Bread cumbs", "a marker to trace our steps"))

bottom_border = f"\n{'=' * (int(len(player.current_room.description)))}\n"
print(bottom_border)
