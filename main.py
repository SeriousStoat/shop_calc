# This is the main menu for the Shop Calculator
# Options in this menu will initiate other Calc instances

from customtkinter import *
from calc import Rpm, Sf

class Header(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = CTkLabel(master=self, text="Welcome to My Shop Calculator",\
                              font=("Tahoma", 30), text_color="orange")
        self.label.grid(row=0, column=0, padx=55, sticky="nsew")
        self.desc = CTkLabel(master=self, justify="left",\
                              text="This application is for helping with machine shop calculations"\
                             "\nPlease select an option to start calculating")
        self.desc.grid(row=1, column=0, padx=55, pady=10, sticky=(W))

class Main(CTk):
    def __init__(self):
        super().__init__()
        # Window and Theme Settings
        self.title("Shop Calculator")
        self.geometry("600x300+300+200")
        self.configure(fg_color="#181b1f", )
        # Heading
        self.header = Header(master=self)
        self.header.grid(row=0, column=0, padx=20, pady=5, sticky="nsew")
        # Content
        self.calcrpm = Rpm(master=self)
        self.calcrpm.grid(row=1, column=0, padx=20, pady=5, sticky="new")
        self.calcsf = Sf(master=self)
        self.calcsf.grid(row=2, column=0, padx=20, pady=5, sticky="new")

       

if __name__ == "__main__":
    app = Main()
    app.mainloop()
