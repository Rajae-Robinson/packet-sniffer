import html
import tkinter as tk
from controller.AuthController import AuthController

class LoginView:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")

        self.username_label = tk.Label(master, text="Username")
        self.username_entry = tk.Entry(master)

        self.password_label = tk.Label(master, text="Password")
        self.password_entry = tk.Entry(master, show='*')

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.master.protocol("WM_DELETE_WINDOW", self.master.quit)

    def login(self):
        # Escape HTML characters
        username = html.escape(self.username_entry.get())
        password = html.escape(self.password_entry.get())
        print(username)
        print(password)
        auth_controller = AuthController()
        auth_controller.login(self.master, username, password)

    def show_login_screen(self):
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
