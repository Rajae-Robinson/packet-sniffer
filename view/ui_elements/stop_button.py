import tkinter as tk
from tkinter import ttk

class StopButton:
    def __init__(self, master):
        self.stop_button = ttk.Button(master, text="Stop Capture")
        self.stop_button.pack(pady=10)
        self.stop_button.configure(state='disabled')

    def set_command(self, command):
        self.stop_button.configure(command=command)

    def configure(self, **kwargs):
        self.stop_button.configure(**kwargs)
