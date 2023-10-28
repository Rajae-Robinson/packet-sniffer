import tkinter as tk
from tkinter import ttk

class FilterUI:
    def __init__(self, master):
        ttk.Label(master, text="Filter by:").pack(pady=5)

        self.filter_type_var = tk.StringVar(value='src')
        ttk.Radiobutton(master, text="Source IP", variable=self.filter_type_var, value='src').pack()
        ttk.Radiobutton(master, text="Destination IP", variable=self.filter_type_var, value='dst').pack()
        ttk.Radiobutton(master, text="Protocol", variable=self.filter_type_var, value='proto').pack()

        self.filter_entry = ttk.Entry(master)
        self.filter_entry.pack()

        self.filter_button = ttk.Button(master, text="Apply Filter")
        self.filter_button.pack(pady=10)

    def set_button_command(self, command):
        self.filter_button.configure(command=command)

    def configure_button(self, **kwargs):
        self.filter_button.configure(**kwargs)

    def get_filter_type(self):
        return self.filter_type_var.get()

    def get_filter_value(self):
        return self.filter_entry.get()
