import tkinter as tk
from .ui_elements.start_button import StartButton
from .ui_elements.stop_button import StopButton
from .ui_elements.filter_ui import FilterUI
from .ui_elements.table_view import TableView
class PacketSnifferView(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Packet Sniffer")

        self.start_button = StartButton(self)
        self.stop_button = StopButton(self)
        self.filter = FilterUI(self)
        self.table = TableView(self)
import tkinter as tk
from .ui_elements.start_button import StartButton
from .ui_elements.stop_button import StopButton
from .ui_elements.filter_ui import FilterUI
from .ui_elements.table_view import TableView
class PacketSnifferView(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Packet Sniffer")

        self.start_button = StartButton(self)
        self.stop_button = StopButton(self)
        self.filter = FilterUI(self)
        self.table = TableView(self)
        self.protocol("WM_DELETE_WINDOW", self.master.quit)