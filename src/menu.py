from design import Color

class Menu:
    """Game menu system"""

    def __init__(self, name, options, instructions):
        self.name = name
        self.options = options
        self.instructions = instructions

    def show_menu(self):
        for k, v in self.options.items():
            print(f"{Color.GREEN}{k.upper()}: {v}{Color.END}")
        print("\n")

    def get_selection(self):
        selection = input(self.instructions).lower().strip()
        return selection


main_menu_options = {
    'm': 'Menu',
    'i': 'Inventory Menu',
    'd': 'Available direction(s) ',
    'q': 'Quit the game',
}

main_menu = Menu("main", main_menu_options,
                 f"Choose a selection or press {Color.GREEN}{Color.BOLD}'m'{Color.END} for the main menu: ")

inventory_menu = {
    'i': 'Inventory Menu',
    'p': 'Player inventory',
    'r': 'Room inventory',
    'm': 'Main menu',
}
inventory_menu = Menu("inventory", inventory_menu,
                      f"Choose from the inventory menu or press {Color.GREEN}{Color.BOLD}'m'{Color.END} to return to the main menu: ")
item_menu = {
    'p': 'Player inventory',
    'r': 'Room inventory',
    'get': 'Get [ITEM_NAME]',
    'drop': 'Drop [ITEM_NAME]',
    'b': 'Previous Menu'
}
item_menu = Menu("item", item_menu,
                 f"GET or DROP an item or press {Color.GREEN}{Color.BOLD}'b'{Color.END} to return to the previous menu: ")
