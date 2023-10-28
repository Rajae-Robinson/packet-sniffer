import threading
from scapy.all import sniff

class PacketSnifferController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.packet_data = []
        self.filter_by = ''  
        self.filter_value = ''

        self.view.set_start_button_command(self.start_capture)
        self.view.set_stop_button_command(self.stop_capture)
        self.view.set_filter_button_command(self.apply_filter)

        self.stop_event = threading.Event()  # Create an event flag

    def start_capture(self):
        self.view.start_button.configure(state='disabled')
        self.view.stop_button.configure(state='normal')
        #self.view.filter_button.configure(state='disabled')

        def process_packet(packet):
            if packet.haslayer('IP'):
                if self.filter_by and self.filter_value !=  '':
                    if self.filter_by == 'src' and packet['IP'].src != self.filter_value:
                        return
                    elif self.filter_by == 'dst' and packet['IP'].dst != self.filter_value:
                        return
                    elif self.filter_by == 'proto' and packet['IP'].proto != int(self.filter_value):
                        return
                
                self.model.add_packet(packet)
                self.view.insert_tree_item((packet['IP'].src, packet['IP'].dst, packet['IP'].proto, packet['IP'].payload))

        # Start packet capturing in a separate thread
        self.stop_event.clear()  # Clear the event flag before capturing
        sniffer_thread = threading.Thread(target=lambda: sniff(prn=process_packet, store=0, stop_filter=lambda p: self.stop_event.is_set()))
        sniffer_thread.start()

    def stop_capture(self):
        self.view.start_button.configure(state='normal')
        self.view.stop_button.configure(state='disabled')
        self.view.filter_button.configure(state='normal')

        # Set the event flag to signal the capturing thread to stop
        self.stop_event.set()

        # Save the captured data to a CSV file
        self.model.save_to_csv('captured_packets.csv')

    def set_filter_by(self, filter_by):
        self.filter_by = filter_by

    def set_filter_value(self, value):
        self.filter_value = value
            
    def apply_filter(self):
        filter_type = self.view.get_filter_type()
        filter_value = self.view.get_filter_value()
        self.set_filter_by(filter_type)
        self.set_filter_value(filter_value)

        # Clear existing data in the Treeview
        for item in self.view.tree.get_children():
            self.view.tree.delete(item)

        # Add filtered data to the Treeview
        for packet in self.model.packet_data:
            self.view.insert_tree_item(packet)
