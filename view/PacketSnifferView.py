import tkinter as tk
from tkinter import ttk

class PacketSnifferView:
    def __init__(self, master):
        self.master = master
        self.master.title("Packet Sniffer")

        # start button
        self.start_button = ttk.Button(master, text="Start Capture")
        self.start_button.pack(pady=10)

        # stop button
        self.stop_button = ttk.Button(master, text="Stop Capture")
        self.stop_button.pack(pady=10)
        self.stop_button.configure(state='disabled')


        # Filter label
        ttk.Label(master, text="Filter by:").pack(pady=5)
        # Filter options
        self.filter_type_var = tk.StringVar(value='src')
        ttk.Radiobutton(master, text="Source IP", variable=self.filter_type_var, value='src').pack()
        ttk.Radiobutton(master, text="Destination IP", variable=self.filter_type_var, value='dst').pack()
        ttk.Radiobutton(master, text="Protocol", variable=self.filter_type_var, value='proto').pack()
        # filter input
        self.filter_entry = ttk.Entry(master)
        self.filter_entry.pack()

        self.filter_button = ttk.Button(master, text="Apply Filter")
        
        self.filter_button.pack(pady=10)

        # Create a Treeview widget for displaying packet data
        #added scrollbar
        tree_frame = tk.Frame(master)
        tree_frame.pack(padx=10, pady=10)

        tree_scrollbar = ttk.Scrollbar(tree_frame)
        tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Table
        self.tree = ttk.Treeview(tree_frame, columns=("Source IP", "Destination IP", "Protocol", "Payload"), show="headings", yscrollcommand=tree_scrollbar.set)
        self.tree.heading("Source IP", text="Source IP")
        self.tree.heading("Destination IP", text="Destination IP")
        self.tree.heading("Protocol", text="Protocol")
        self.tree.heading("Payload", text="Payload")
        self.tree.pack(side=tk.LEFT)

        tree_scrollbar.config(command=self.tree.yview)
        self.tree.pack(padx=10, pady=10)
        

    def set_start_button_command(self, command):
        self.start_button.configure(command=command)

    def set_stop_button_command(self, command):
        self.stop_button.configure(command=command)

    def set_filter_button_command(self, command):
        self.filter_button.configure(command=command)

    def insert_tree_item(self, values):
        self.tree.insert("", "end", values=values)
        
    def get_filter_type(self):
        return self.filter_type_var.get()
    
    def get_filter_value(self):
        return self.filter_entry.get()
    
    def insert_tree_item(self, values):
        item_id = self.tree.insert("", "end", values=values)
        # Auto-scroll to the newest entry
        self.tree.see(item_id)