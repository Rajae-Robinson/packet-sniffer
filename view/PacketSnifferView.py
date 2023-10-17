# view.py

import tkinter as tk
from tkinter import ttk

class PacketSnifferView:
    def __init__(self, master):
        self.master = master
        self.master.title("Packet Sniffer")

        self.start_button = ttk.Button(master, text="Start Capture")
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(master, text="Stop Capture")
        self.stop_button.pack(pady=10)
        self.stop_button.configure(state='disabled')

        ttk.Label(master, text="Filter by Source/Destination IP:").pack(pady=5)
        self.ip_filter_entry = ttk.Entry(master)
        self.ip_filter_entry.pack()

        self.filter_button = ttk.Button(master, text="Apply Filter")
        self.filter_button.pack(pady=10)

        # Create a Treeview widget for displaying packet data
        self.tree = ttk.Treeview(master, columns=("Source IP", "Destination IP", "Protocol", "Payload"), show="headings")
        self.tree.heading("Source IP", text="Source IP")
        self.tree.heading("Destination IP", text="Destination IP")
        self.tree.heading("Protocol", text="Protocol")
        self.tree.heading("Payload", text="Payload")
        self.tree.pack(padx=10, pady=10)

    def set_start_button_command(self, command):
        self.start_button.configure(command=command)

    def set_stop_button_command(self, command):
        self.stop_button.configure(command=command)

    def set_filter_button_command(self, command):
        self.filter_button.configure(command=command)

    def get_ip_filter(self):
        return self.ip_filter_entry.get()

    def insert_tree_item(self, values):
        self.tree.insert("", "end", values=values)
