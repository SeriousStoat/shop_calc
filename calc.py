# This program calculates sf + dia to get rpm
# Testing CustomTkInter Module

from customtkinter import *
from math import pi

class Rpm(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # SF Input
        CTkLabel(master=self, text="Surface Footage:").grid(column=2, row=1, sticky="e")
        self.sf = StringVar()
        sf_entry = CTkEntry(master=self, width=50, textvariable=self.sf)
        sf_entry.grid(column=3, row=1, padx=5)
        # Dia Input
        CTkLabel(master=self, text="Part or Cutter Dia:").grid(column=2, row=2, padx="40 0", sticky="e")
        self.dia = StringVar()
        dia_entry = CTkEntry(master=self, width=50, textvariable=self.dia)
        dia_entry.grid(column=3, row=2)
        
        # RPM Output
        self.rpm = StringVar()
        CTkLabel(master=self, width=40, justify="right", textvariable=self.rpm).grid(column=4, row=1, rowspan=2, padx=5, sticky="e")
        CTkLabel(master=self, text=" RPMs").grid(column=5, row=1, rowspan=2, sticky="w")

        # Calculate Button
        self.calc= CTkButton(master=self, text="Calculate RPMs", command=self.calculate)
        self.calc.grid(column=1, row=1, rowspan=2, pady=5, padx=5)

    def calculate(self, *args):
        try:
            get_sf = int(self.sf.get())
            get_dia = float(self.dia.get())
            self.rpm.set(round((get_sf*12)/(pi*get_dia)))
        except ValueError:
            pass

class Sf(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # RPM Input
        CTkLabel(master=self, text="RPMs:").grid(column=2, row=1, sticky="e")
        self.rpm = StringVar()
        sf_entry = CTkEntry(master=self, width=50, textvariable=self.rpm)
        sf_entry.grid(column=3, row=1, padx=5)
        # Dia Input
        CTkLabel(master=self, text="Part or Cutter Dia:").grid(column=2, row=2, padx="40 0", sticky="e")
        self.dia = StringVar()
        dia_entry = CTkEntry(master=self, width=50, textvariable=self.dia)
        dia_entry.grid(column=3, row=2)
        
        # RPM Output
        self.sf = StringVar()
        CTkLabel(master=self, width=40, justify="right", textvariable=self.sf).grid(column=4, row=1, rowspan=2, padx=5, sticky="e")
        CTkLabel(master=self, text=" Feet per Minute").grid(column=5, row=1, rowspan=2, sticky="w")

        # Calculate Button
        self.calc= CTkButton(master=self, text="Calculate SF", command=self.calculate)
        self.calc.grid(column=1, row=1, rowspan=2, pady=5, padx=5)

    def calculate(self, *args):
        try:
            get_rpm = int(self.rpm.get())
            get_dia = float(self.dia.get())
            self.sf.set(round((get_rpm*pi*get_dia)/12))
        except ValueError:
            pass

            

