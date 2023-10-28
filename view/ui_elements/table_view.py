import tkinter as tk
from tkinter import ttk

class TableView:
    def __init__(self, master):
        tree_frame = tk.Frame(master)
        tree_frame.pack(padx=10, pady=10)

        tree_scrollbar = ttk.Scrollbar(tree_frame)
        tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(tree_frame, columns=("Source IP", "Destination IP", "Protocol", "Payload"), show="headings", yscrollcommand=tree_scrollbar.set)
        self.tree.heading("Source IP", text="Source IP")
        self.tree.heading("Destination IP", text="Destination IP")
        self.tree.heading("Protocol", text="Protocol")
        self.tree.heading("Payload", text="Payload")
        self.tree.pack(side=tk.LEFT)

        tree_scrollbar.config(command=self.tree.yview)
        self.tree.pack(padx=10, pady=10)

    def insert_item(self, values):
        item_id = self.tree.insert("", "end", values=values)
        # Auto-scroll to the newest entry
        self.tree.see(item_id)
    
    def get_tree(self):
        return self.tree
