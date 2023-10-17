import threading
from scapy.all import sniff, IP

class PacketSnifferController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.set_start_button_command(self.start_capture)
        self.view.set_stop_button_command(self.stop_capture)
        self.view.set_filter_button_command(self.apply_filter)

        self.stop_event = threading.Event()  # Create an event flag

    def start_capture(self):
        self.view.start_button.configure(state='disabled')
        self.view.stop_button.configure(state='normal')
        self.view.filter_button.configure(state='disabled')

        def process_packet(packet):
            if packet.haslayer('IP'):
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

        # Wait for the sniffer thread to finish
        # sniffer_thread.join()

    def apply_filter(self):
        filter_ip = self.view.get_ip_filter()
        # Use filter_ip in your packet filtering logic
