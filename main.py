# This is the main menu for the Shop Calculator
# Options in this menu will initiate other Calc instances

from customtkinter import *
from calc import Rpm, Sf

class Header(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwagit rgs)
        self.label = CTkLabel(master=self, text="My Shop Calculator", font=("Tahoma", 30), text_color="orange")
        self.label.grid(row=0, column=0, padx=55, pady=20, sticky="nsew")

class Main(CTk):
    def __init__(self):
        super().__init__()
        # Window and Theme Settings
        self.title("Shop Calculator")
        self.geometry("600x400+300+200")
        self.configure(fg_color="#181b1f")
        self.columnconfigure(1, weight=1)
        # Heading
        self.header = Header(master=self, corner_radius=0)
        self.header.grid(row=0, column=0, columnspan=3, pady=5, sticky="nsew")
        # Content
        self.calcrpm = Rpm(master=self, corner_radius=0)
        self.calcrpm.grid(row=1, column=0, columnspan=3, pady=5, sticky="new")
        self.calcsf = Sf(master=self, corner_radius=0)
        self.calcsf.grid(row=2, column=0, columnspan=3, pady=5, sticky="new")

if __name__ == "__main__":
    app = Main()
    app.mainloop()
