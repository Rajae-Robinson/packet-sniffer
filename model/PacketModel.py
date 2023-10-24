import csv

class PacketModel:
    def __init__(self):
        self.packet_data = []
        self.filter_by = 'src'  # Default filter by source IP

    def set_filter_by(self, filter_by):
        self.filter_by = filter_by

    def add_packet(self, packet):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        protocol = packet['IP'].proto
        payload = packet['IP'].payload

        if self.filter_by == 'src':
            if src_ip == self.view.get_ip_filter():
                self.packet_data.append([src_ip, dst_ip, protocol, payload])
        else:
            if dst_ip == self.view.get_ip_filter():
                self.packet_data.append([src_ip, dst_ip, protocol, payload])
    def add_packet(self, packet):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        protocol = packet['IP'].proto
        payload = packet['IP'].payload

        self.packet_data.append([src_ip, dst_ip, protocol, payload])

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.packet_data)
