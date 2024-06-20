# This program calculates sf + dia to get rpm
# Testing CustomTkInter Module

from customtkinter import *
from math import pi

class Rpm_Calc(CTk):
    def __init__(self):
        super().__init__()
        # Window and Theme Settings
        self.title("Shop Calculator")
        self.evwidth = 400 #width of entry widget
        self.bwidth1 = self.evwidth/4 - 20
        self.configure(fg_color="#181b1f")
        # SF Input
        CTkLabel(master=self, text="Enter your Surface Footage: ").grid(column=1, row=1, sticky=(E))
        self.sf = StringVar()
        sf_entry = CTkEntry(master=self, width=50, textvariable=self.sf)
        sf_entry.grid(column=2, row=1, sticky=(W, E))
        CTkLabel(master=self, text=" Feet per Minute ").grid(column=3, row=1, sticky=(W))
        # Dia Input
        CTkLabel(master=self, text="Enter your part Diamiter: ").grid(column=1, row=2, sticky=(E))
        self.dia = StringVar()
        dia_entry = CTkEntry(master=self, width=50, textvariable=self.dia)
        dia_entry.grid(column=2, row=2, sticky=(W, E))
        CTkLabel(master=self, text=" Inches ").grid(column=3, row=2, sticky=(W))
        # RPM Output
        self.rpm = StringVar()
        CTkLabel(master=self, text="Set your Spindle RPMs to: ").grid(column=1, row=3, sticky=(E))
        CTkLabel(master=self, textvariable=self.rpm).grid(column=2, row=3, sticky=(W))
        self.calc= CTkButton(master=self, text="Calculate", command=self.calculate, width=self.bwidth1)
        self.calc.grid(row=4, column=1, pady=15, padx=20)



    def calculate(self, *args):
        try:
            get_sf = int(self.sf.get())
            get_dia = float(self.dia.get())
            self.rpm.set(int((get_sf*12)/(pi*get_dia)))
        except ValueError:
            pass

if __name__ == "__main__":
    app = Rpm_Calc()
    app.mainloop()


            

