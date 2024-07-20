# This is the main menu for the Shop Calculator
# Options in this menu will initiate other Calc instances

from customtkinter import CTk, CTkFrame, CTkLabel, CTkImage, CTkButton
from PIL import Image
from calc import SpeedFeed
from info import Info

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
        self.geometry("600x515+200+200")
        self.columnconfigure(1, weight=1)

        # Header Frame
        self.header = Header(master=self, corner_radius=0)
        self.header.grid(row=0, column=0, columnspan=3, pady=5, sticky="nsew")

        def infoWindow():
            info_window = Info(master=self)

        info_image = CTkImage(light_image=Image.open('info.png'),
                                          dark_image=Image.open('info.png'),
                                          size=(15, 15))
        info_button = CTkButton(master=self.header, text='', image=info_image, width=15, height=15,
                                fg_color="transparent", border_width=0, border_spacing=0, command=infoWindow)
        info_button.place(relx=.94,rely=.1)

        # Content
        self.speed_feed = SpeedFeed(master=self, corner_radius=0)
        self.speed_feed.grid(row=1, column=0, columnspan=3, pady=5, sticky="new")

if __name__ == "__main__":
    app = Main()
    app.mainloop()
