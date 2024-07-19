# This module is separated so that it can interact with both the main app and modules
from customtkinter import CTkFrame, CTkLabel, CTkFont

class MsgBar(CTkFrame):# Content Frames
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = CTkLabel(master=self, font=CTkFont(family="Georgia"))
        self.label.pack()