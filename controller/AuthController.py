
from view.PacketSnifferView import PacketSnifferView
from model.UserDatabase import UserDatabase
from controller.PacketSnifferController import PacketSnifferController

class AuthController:
    def __init__(self):
        self.logged_in = False
        self.user_db = UserDatabase()

    def login(self, view, username, password):
        hashed_password = self.user_db.get_password(username)
        if hashed_password and self.user_db.check_password(password, hashed_password[0]):
            self.logged_in = True
            view.withdraw()
            PacketSnifferController(PacketSnifferView())

        else:
            print("Invalid credentials")
