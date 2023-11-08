import tkinter as tk
from view.LoginView import LoginView

if __name__ == "__main__":
    root = tk.Tk()
    LoginView(root).show_login_screen()
    root.mainloop()
