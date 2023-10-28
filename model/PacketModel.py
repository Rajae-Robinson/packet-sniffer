import csv

class PacketModel:
    def __init__(self):
        self.packet_data = []

    def add_packet(self, packet):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        protocol = packet['IP'].proto
        payload = packet['IP'].payload
        
        self.packet_data.append((src_ip, dst_ip, protocol, payload))

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.packet_data)
