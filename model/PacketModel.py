from tkinter import messagebox
import csv
import logging

class PacketModel:
    def __init__(self):
        self.packet_data = []

    def add_packet(self, packet):
        try: 
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst
            protocol = packet['IP'].proto
            payload = packet['IP'].payload
            
            self.packet_data.append((src_ip, dst_ip, protocol, payload))
        except KeyError as e:
            print(f"KeyError: {e} not found in packet  ")
            logging.error(e)
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(e)
            
    def save_to_csv(self, filename):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.packet_data)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save captured packets: {e}")
            logging.error(e)
