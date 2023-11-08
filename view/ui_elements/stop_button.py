import tkinter as tk
from tkinter import ttk

class StopButton:
    def __init__(self, master):
        self.stop_button = tk.Button(master, text="Stop Capture", background='orange red')
        self.stop_button.pack(pady=10)
        self.stop_button.configure(state='disabled')

    def set_command(self, command):
        self.stop_button.configure(command=command)

    def configure(self, **kwargs):
        self.stop_button.configure(**kwargs)
