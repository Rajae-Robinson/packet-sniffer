from .ui_elements.start_button import StartButton
from .ui_elements.stop_button import StopButton
from .ui_elements.filter_ui import FilterUI
from .ui_elements.table_view import TableView
class PacketSnifferView:
    def __init__(self, master):
        self.master = master
        self.master.title("Packet Sniffer")

        self.start_button = StartButton(master)
        self.stop_button = StopButton(master)
        self.filter = FilterUI(master)
        self.table = TableView(master)
