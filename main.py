"""
Project Members:
Cassandra Powell (2005742)
Leondre Bromfield (2000070)
Onieka Saunders (1800249)
Rajae Robinson (2006677)

Tutor: Mr. Kevin Johnson
"""

import tkinter as tk
from view.LoginView import LoginView

if __name__ == "__main__":
    root = tk.Tk()
    LoginView(root).show_login_screen()
    root.mainloop()
