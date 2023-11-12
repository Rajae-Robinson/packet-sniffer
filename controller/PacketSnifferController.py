import threading
import ipaddress
import time
from tkinter import messagebox
import logging
from scapy.all import sniff
from model.PacketModel import PacketModel
from view.SummaryView import SummaryView

class PacketSnifferController:
    def __init__(self, view):
        self.model = PacketModel()
        self.view = view
        self.packet_data = []
        self.filter_by = ''  
        self.filter_value = ''

        # Initialize variables for statistics
        self.start_time = None
        self.end_time = None
        self.protocol_counter = {}  # Dictionary to count protocols
        self.total_packet_size = 0
        self.num_packets = 0
    
        self.view.start_button.set_command(self.start_capture)
        self.view.stop_button.set_command(self.stop_capture)
        self.view.filter.set_button_command(self.apply_filter)

        self.stop_event = threading.Event()  # Create an event flag

    def start_capture(self):
        try:
            self.start_time = time.time()
            self.view.start_button.configure(state='disabled')
            self.view.stop_button.configure(state='normal')

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
            
                    # Update total packet size
                    self.total_packet_size += len(packet['IP'].payload)
                    # Update total number of packets captured
                    self.num_packets += 1

            # Start packet capturing in a separate thread
            self.stop_event.clear()  # Clear the event flag before capturing
            sniffer_thread = threading.Thread(target=lambda: sniff(prn=process_packet, store=0, stop_filter=lambda p: self.stop_event.is_set()))
            sniffer_thread.start()

        except Exception as e:
            print(f"An error occurred in start_capture: {e}")
            logging.error(e)

    def stop_capture(self):
        try:
            self.end_time = time.time()
            self.view.start_button.configure(state='normal')
            self.view.stop_button.configure(state='disabled')
            self.view.filter.configure_button(state='normal')

            # Calculate capture duration
            capture_duration = self.end_time - self.start_time

            # Calculate average packet size
            average_packet_size = self.total_packet_size / self.num_packets if self.num_packets > 0 else 0

            # Set the event flag to signal the capturing thread to stop
            self.stop_event.set()

            # Save the captured data to a CSV file
            self.model.save_to_csv('captured_packets.csv')

            self.summary_view = SummaryView()
            # Update the Summary View with the gathered information
            self.summary_view.update_summary(self.num_packets, capture_duration, average_packet_size)
            # Show Summary View
            self.summary_view.showSummaryScreen()

        except Exception as e:
            print(f"An error occurred while trying to stop: {e}")
            logging.error(e)

    def set_filter_by(self, filter_by):
        try:
            self.filter_by = filter_by
        except Exception as e:
            print("An error occurred while trying to set filter: {e}")
            logging.error(e)

    def set_filter_value(self, value):
        try:
            self.filter_value = value
        except Exception as e:
            print("An error occurred while trying to set filter: {e}")
            logging.error(e)
       

    def apply_filter(self):
        try:
            filter_type = self.view.filter.get_filter_type()
            filter_value = self.view.filter.get_filter_value()
            if filter_type in ['src', 'dst']:
                try:
                    ipaddress.IPv4Address(filter_value)
                except ValueError:
                    messagebox.showerror("Invalid IP Address", "Please enter a valid IP address.")
                    return
            if filter_type == 'proto' and not(filter_value.isdigit()):
                messagebox.showerror("Invalid Protocol", "Protocol should be a number.")
                return

            self.set_filter_by(filter_type)
            self.set_filter_value(filter_value)
            messagebox.showinfo("Success", f"Filter successfully applied.")
        except Exception as e:
            print("An error occurred while trying to apply filter: {e}")
            logging.error(e)
