import tkinter as tk

class SummaryView(tk.Toplevel):
    def __init__(self):
        super().__init__() 
        self.geometry('500x500')  
        self.title("Summary Report")  
        
        self.num_packets_label = tk.Label(self, text="Number of Packets Captured:")

        self.capture_duration_label = tk.Label(self, text="Capture Duration:")

        self.average_packet_size_label = tk.Label(self, text="Average Packet Size:")
        

    
    def update_summary(self, num_packets, capture_duration, average_packet_size):
        self.num_packets_label.config(text=f"Number of Packets Captured: {num_packets}")
        self.capture_duration_label.config(text=f"Capture Duration: {capture_duration:.2f} seconds")
        self.average_packet_size_label.config(text=f"Average Packet Size: {average_packet_size:.2f} bytes")

    def showSummaryScreen(self):
        self.num_packets_label.pack()
        self.capture_duration_label.pack()
        self.average_packet_size_label.pack()