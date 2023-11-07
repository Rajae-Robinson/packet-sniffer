import threading
from scapy.all import sniff
from model.PacketModel import PacketModel

class PacketSnifferController:
    def __init__(self, view):
        try:
            self.model = PacketModel()
            self.view = view
            self.packet_data = []
            self.filter_by = ''  
            self.filter_value = ''
        
            self.view.start_button.set_command(self.start_capture)
            self.view.stop_button.set_command(self.stop_capture)
            self.view.filter.set_button_command(self.apply_filter)

            self.stop_event = threading.Event()  # Create an event flag
        except Exception as e:
            print(f"An error occurred in __init__: {e}")

    def start_capture(self):
        try:
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
                    self.view.table.insert_item((packet['IP'].src, packet['IP'].dst, packet['IP'].proto, packet['IP'].payload))

            # Start packet capturing in a separate thread
            self.stop_event.clear()  # Clear the event flag before capturing
            sniffer_thread = threading.Thread(target=lambda: sniff(prn=process_packet, store=0, stop_filter=lambda p: self.stop_event.is_set()))
            sniffer_thread.start()
        except Exception as e:
            print(f"An error occurred in start_capture: {e}")

    def stop_capture(self):
        try:
            self.view.start_button.configure(state='normal')
            self.view.stop_button.configure(state='disabled')
            self.view.filter.configure_button(state='normal')

            # Set the event flag to signal the capturing thread to stop
            self.stop_event.set()

            # Save the captured data to a CSV file
            self.model.save_to_csv('captured_packets.csv')
        except Exception as e:
            print(f"An error occurred while trying to stop: {e}")

    def set_filter_by(self, filter_by):
        try:
            self.filter_by = filter_by
        except Exception as e:
            print("An error occurred while trying to set filter: {e}")

    def set_filter_value(self, value):
        try:
            self.filter_value = value
        except Exception as e:
            print("An error occurred while trying to set filter: {e}")
            
    def apply_filter(self):
        try: 
            filter_type = self.view.filter.get_filter_type()
            filter_value = self.view.filter.get_filter_value()
            self.set_filter_by(filter_type)
            self.set_filter_value(filter_value)
        except Exception as e:
            print("An error occurred while trying to apply filter: {e}")
