# This module is separated so that it can interact with both the main app and modules
from customtkinter import *

class Msg(CTkFrame):# Content Frames
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.msg = StringVar()
        self.label = CTkLabel(master=self, textvariable=self.msg, text_color="#e0e0e0", font=CTkFont(family="Georgia"))
        self.label.pack()

