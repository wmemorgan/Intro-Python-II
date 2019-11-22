class Menu:
    """Game menu system"""

    def __init__(self, name, options, instructions):
        self.name = name
        self.options = options
        self.instructions = instructions

    def show_menu(self):
        for k, v in self.options.items():
            print(f"{k.upper()}: {v}")
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
                 "Choose a selection or press 'm' for the main menu: ")

inventory_menu = {
    'i': 'Inventory Menu',
    'p': 'Player inventory',
    'r': 'Room inventory',
    'm': 'Main menu',
}
inventory_menu = Menu("inventory", inventory_menu,
                      "Choose from the inventory menu or press 'm' to return to the main menu: ")
item_menu = {
    'p': 'Player inventory',
    'r': 'Room inventory',
    'get': 'Get [ITEM_NAME]',
    'drop': 'Drop [ITEM_NAME]',
    'b': 'Previous Menu'
}
item_menu = Menu("item", item_menu,
                 "GET or DROP an item or press 'b' to return to the previous menu: ")
