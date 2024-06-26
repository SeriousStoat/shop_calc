# This is the main menu for the Shop Calculator
# Options in this menu will initiate other Calc instances

from customtkinter import *
from calc import SpeedFeed

class Header(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = CTkLabel(master=self, text="My Shop Calculator", font=("Tahoma", 30))
        self.label.pack(fill="both", expand=True, padx=30, pady=20)

class Main(CTk):
    def __init__(self):
        super().__init__()
        # Window and Theme Settings
        self.title("Shop Calculator")
        self.geometry("600x400+300+200")
        self.columnconfigure(1, weight=1)

        # Header Frame
        self.header = Header(master=self, corner_radius=0)
        self.header.grid(row=0, column=0, columnspan=3, pady=5, sticky="nsew")

        # Content
        self.speed_feed = SpeedFeed(master=self, corner_radius=0)
        self.speed_feed.grid(row=1, column=0, columnspan=3, pady=5, sticky="new")

        self.bind('<Return>', self.focus)

    def focus(self, *args):
        if self.focus_get() == ".!speedfeed.!ctkframe.!ctkentry.!entry" or ".!speedfeed.!ctkframe.!ctkentry2.!entry":
            self.bind('<Return>', self.speed_feed.calc_rpm)

if __name__ == "__main__":
    app = Main()
    app.mainloop()
