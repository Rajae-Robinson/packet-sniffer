import tkinter as tk
from controller.PacketSnifferController import PacketSnifferController
from model.PacketModel import PacketModel
from view.PacketSnifferView import PacketSnifferView

if __name__ == "__main__":
    root = tk.Tk()
    model = PacketModel()
    view = PacketSnifferView(root)
    controller = PacketSnifferController(model, view)
    root.mainloop()
