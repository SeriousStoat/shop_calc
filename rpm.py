# This program calculates sf + dia to get rpm
# Testing CustomTkInter Module

from customtkinter import *
from math import pi

class App(CTk):
    def __init__(self):
        super.()__init__()
        self.title("Shop Calculator")
        self.evwidth = 400 #width of entry widget
        self.bwidth1 = self.evwidth/4 - 20
        self.configure(fg_color="#181b1f")
        self.values = CTkEntry(master=self, width=self.evwidth)
        self.values.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.calc= CTkButton(master=self, text="Calculate", command=self.evaluate, width=self.bwidth1)
        self.calc.grid(row=4, column=1, pady=5, padx=10)
    def calc_rpm(*arg):
        get_sf = sf(get())
        get_dia = dia(get())
        lambda sf, dia: rpm((sf_get*12)/(pi*get_dia))

