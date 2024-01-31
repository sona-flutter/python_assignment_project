from typing import self
from PIL import Image,ImageTk
import tkinter as tk
import os
from tkinter import ttk,messagebox

class C2W_TkinterLibraryApp:
    def __init__(self):
        
        #Initializevth Tkinter root window
        self.c2w_root=tk.Tk()
        self.c2w_screen_width=self.c2w_root.winfo_screenwidth()
        self.c2w_screen_height=self.c2w_root.winfo_screenwidth()
        self.c2w_root.title("Tkinter Library")
    
self.c2w_root.geometry(f"{self.c2w_screen_width}x{self.c2w_scrren_height}")
self.c2w_root.configure(bg="#192f44")

#Set up th UI companents
self.setup_ui()

def setup_ui(self):
    
    #Create the main background frame
    self.c2w_left_frame=tk.Frame(self.c2w_background_frame, bg="#0A2472",width=self.c2w_screen_width, height=self.c2w_screen_height)
    self.c2w_background_frame.pack()
    
    #Create the left frame for navigation and buttons
    self.c2w_left_frame=tk.Frame(self.c2w_background_frame, bg="00-72D",width=self.c2w_screen_width, height=self.c2w_screen_height)
    self.c2w_left_frame.pack(side=tk.LEFT)
    
    #Set up button styling
    style=ttk.Style()
    style.configure("Rounded.TButton",borderwidth=0,relief="flat",background="#BCD2E8",padding=10,font=("Poppins",12))
    style.map("Rounded TButton",foreground=[('pressed','black'),('active','white')])
    
    #Create the font Library button
    self.c2w
    