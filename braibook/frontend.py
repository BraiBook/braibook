import yaml
from .preferences import Preferences


class frontend (Preferences):
    "Menu navigation and preference management class"
    ACTION_ID = {
        'FORWARD': 0,
        'BACKWARD': 1,
        'UP': 2,
        'DOWN': 3,
        'CENTER': 4}

    MENU_PATH = 'resources/menu.yml'

    def load_menu(self):
        return yaml.load(open(self.MENU_PATH, 'r'))

    def open_submenu(self):
        self.menu = self.menu.append(self.menu[1])

    def open_supermenu(self):
        self.menu = self.menu.pop()

    def menu_show_next(self):
        print("TODO")

    def menu_show_previous(self):
        print("TODO")

    def update_display(self):
        # TODO represent menu string in BB device
        print("TODO")

    def handler(self, ACTION_ID, MENU_ID):
        if len(self.menu) != 1:
            # DEFAULT NAVIGATION HANDLER
            if ACTION_ID == 'FORWARD':
                self.menu_show_next()
            elif ACTION_ID == 'BACKWARD':
                self.menu_show_previous()
            elif ACTION_ID == 'UP':
                self.open_supermenu()
            elif (ACTION_ID == 'CENTER' | ACTION_ID == 'DOWN'):
                self.open_submenu()

        else:
            # SPECIFIC HANDLER
            if MENU_ID == 'PLAY':
                print("TODO")
            elif MENU_ID == 'OPEN':
                print("TODO")
            elif MENU_ID == 'LANGUAGE':
                print("TODO")
            elif MENU_ID == 'SET_DEFAULT_SPEED':
                print("TODO")
            elif MENU_ID == 'SET_ENCODING':
                print("TODO")
            elif MENU_ID == 'LECTURE_TYPE':
                print("TODO")
            elif MENU_ID == 'BRAILLE_SYSTEM':
                print("TODO")

    def __init__(self):
        self.menu = [self.load_menu(self)]
        self.menu_id = self.menu[0]
