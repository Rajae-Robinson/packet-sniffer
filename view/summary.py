import tkinter as tk
from tkinter import Label, Tk, ttk

def __init__(self, master):
    base = Tk()  
    base.geometry('500x500')  
    base.title("Registration Form")  
    
    labl_0 = Label(base, text="Summary Report",width=20,font=("bold", 20))  
    labl_0.place(x=90,y=53)  

    labl_1 = Label(base, text="IP entered: ",width=20,font=("bold", 10))  
    labl_1.place(x=80,y=130)  
    #call ip entered or protocol number 

    labl_2 = Label(base, text="Destinations IP",width=20,font=("bold", 10))  
    labl_2.place(x=68,y=180)  