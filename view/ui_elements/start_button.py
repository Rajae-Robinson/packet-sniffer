import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk

class StartButton:
    
    def __init__(self, master):
        self.start_button = tk.Button(master, text="Start Capture", background='pale green')
        #self.configure(bg = "green")
        self.start_button.pack(pady=10)

    def set_command(self, command):
        self.start_button.configure(command=command)

    def configure(self, **kwargs):
        self.start_button.configure(**kwargs)
