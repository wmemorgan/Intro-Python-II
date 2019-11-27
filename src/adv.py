import re
from menu import main_menu, inventory_menu, item_menu
from player import Player
from locations import room
from inventory import Inventory
from item import Item, Gold, Food
from design import Color

# Make a new player object that is currently in the 'outside' room.
player = Player('George', room['outside'], Inventory(
    'Player Inventory', [Gold(10), Food('apple', 'red delicious', 5)]))
# player = Player('Harry', room['outside'], Inventory('Player Inventory', [Item(
#     'Magic Wand', 'used for casting spells'), Item('Broom', 'used for transportation and sport')]))

# REPL (Read, evaluate, print, loop)
selection = ''
padding = len("located in, carries the following items:") + 4
top_border = f"{'=' * (int(len(player.name+player.current_room.name)+padding))}"
print(top_border)
print(player)
print(f'{player.current_room.description}\n')
main_menu.show_menu()
player.current_room.show_available_directions()

while selection != 'q':
    selection = main_menu.get_selection()

    if selection == 'q':
        print(f"\n{Color.BLUE}{Color.BOLD}THANK YOU FOR PLAYING!{Color.END}")
    elif selection == 'm':
        main_menu.show_menu()
    elif selection == 'd':
        player.current_room.show_available_directions()
    elif selection == 'i':
        inv_selection = ''

        while inv_selection != 'm':
            inventory_menu.show_menu()
            inv_selection = inventory_menu.get_selection()

            if inv_selection == 'm':
                main_menu.show_menu()
            elif inv_selection == 'i':
                inventory_menu.show_menu()
            elif inv_selection == 'p':
                if (len(player.inventory.items) > 0):
                    print("\nYou are carrying the following items:")
                print(player.inventory.show_inventory())

                item_selection = ''

                while item_selection != 'b':
                    item_menu.show_menu()
                    item_selection = item_menu.get_selection()
                    item_selection = re.sub(" +", " ", item_selection)

                    if item_selection == 'b':
                        print("\nReturn to previous menu\n")
                    elif item_selection[:3] == 'get':
                        player.get_item(item_selection[3:].strip())
                    elif item_selection[:4] == 'drop':
                        player.drop_item(item_selection[4:].strip())
                    elif item_selection == 'p':
                        if (len(player.inventory.items) > 0):
                            print("\nYou are carrying the following items:")
                        print(player.inventory.show_inventory())
                    elif item_selection == 'r':
                        if (len(player.current_room.inventory.items) > 0):
                            print(f"{player.current_room.name} contains:")
                        print(player.current_room.inventory.show_inventory())
                    else:
                        print(f"\n{Color.RED}Invalid entry, please try again.{Color.END}\n")
                    
            elif inv_selection == 'r':
                if (len(player.current_room.inventory.items) > 0):
                    print(f"\n{Color.CYAN}{player.current_room.name}{Color.END} contains:")
                print(player.current_room.inventory.show_inventory())

                item_selection = ''

                while item_selection != 'b':
                    item_menu.show_menu()
                    item_selection = item_menu.get_selection()
                    item_selection = re.sub(" +", " ", item_selection)
                    if item_selection == 'b':
                        print("\nReturn to previous menu\n")
                    elif item_selection[:3] == 'get':
                        player.get_item(item_selection[3:].strip())
                    elif item_selection[:4] == 'drop':
                        player.drop_item(item_selection[4:].strip())
                    elif item_selection == 'p':
                        if (len(player.inventory.items) > 0):
                            print("\nYou are carrying the following items:")
                        print(player.inventory.show_inventory())
                    elif item_selection == 'r':
                        if (len(player.current_room.inventory.items) > 0):
                            print(f"\n{player.current_room.name} contains:")
                        print(player.current_room.inventory.show_inventory())
                    else:
                        print(f"\n{Color.RED}Invalid entry, please try again.{Color.END}\n")

            else:
                print(f"\n{Color.RED}Invalid entry, please try again.{Color.END}\n")

    elif selection not in player.current_room.get_available_directions():
        print(f"\n{Color.RED}Error, please enter valid direction:{Color.END}\n")
    else:
        player.change_room(selection)
        player.current_room.show_available_directions()

bottom_border = f"\n{'=' * (int(len(player.name+player.current_room.name)+padding))}\n"
print(bottom_border)
