# This program calculates sf + dia to get rpm
# Testing CustomTkInter Module

from customtkinter import *
from math import pi
from msg import Msg

class SpeedFeed(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Message Bar
        self.msg_frame = Msg(master=self, corner_radius=5, fg_color="#181818", width=600)
        self.msg_frame.pack(fill="both", expand=True, padx=30, pady=5)
        self.msg_frame.msg.set("Speeds & Feeds: Fill out a form and click 'Calculate'")

        # Rpm Frame
        rpm_frame = CTkFrame(master=self, corner_radius=0)
        rpm_frame.pack(fill="both", expand=True, pady=5)

            # Calculate Button
        self.calc = CTkButton(master=rpm_frame, text="Calculate RPMs", command=self.calc_rpm)
        self.calc.grid(column=1, row=1, rowspan=2, pady=5, padx=5)

            # SF Input
        CTkLabel(master=rpm_frame, text="Surface Footage = ").grid(column=2, row=1, sticky="e")
        self.sf = StringVar()
        sf_entry = CTkEntry(master=rpm_frame, width=50, textvariable=self.sf)
        sf_entry.grid(column=3, row=1, padx=5)

            # Dia Input
        CTkLabel(master=rpm_frame, text="Part or Cutter Dia = ").grid(column=2, row=2, padx="40 0", sticky="e")
        self.dia = StringVar()
        dia_entry = CTkEntry(master=rpm_frame, width=50, textvariable=self.dia)
        dia_entry.grid(column=3, row=2)
        
            # RPM Output
        self.rpm = StringVar()
        CTkLabel(master=rpm_frame, text=">").grid(column=4, row=1, rowspan=2, padx=5, sticky="e")
        CTkLabel(master=rpm_frame, width=40, justify="right", textvariable=self.rpm, text_color="orange")\
            .grid(column=5, row=1, rowspan=2, padx=5, sticky="e")

    def calc_rpm(self, *args):
        try:
            get_sf = int(self.sf.get())
            get_dia = float(self.dia.get())
            give_rpm = (round((get_sf*12)/(pi*get_dia)))
            self.rpm.set(f"{give_rpm} rpm")
            # Message
            self.msg_frame.msg.set("RPMs Calculated")
            self.msg_frame.label.configure(text_color="green")
            
        except ValueError:
            self.msg_frame.msg.set("Calculation Error : Please enter valid numbers.")
            self.msg_frame.label.configure(text_color="Tomato")
            self.rpm.set("")
        except ZeroDivisionError:
            self.msg_frame.msg.set("Calculation Error : Cannot divide by zero.")
            self.msg_frame.label.configure(text_color="Tomato")
            self.rpm.set("")
     # This needs to be incorperated into the SpeedsFeeds class   
# class Sf(CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         # Calculate Button
#         self.calc= CTkButton(master=self, text="Calculate SF", command=self.calculate)
#         self.calc.grid(column=1, row=1, rowspan=2, pady=5, padx=5)

#         # RPM Input
#         CTkLabel(master=self, text="RPMs:").grid(column=2, row=1, sticky="e")
#         self.rpm = StringVar()
#         sf_entry = CTkEntry(master=self, width=50, textvariable=self.rpm)
#         sf_entry.grid(column=3, row=1, padx=5)

#         # Dia Input
#         CTkLabel(master=self, text="Part or Cutter Dia:").grid(column=2, row=2, padx="40 0", sticky="e")
#         self.dia = StringVar()
#         dia_entry = CTkEntry(master=self, width=50, textvariable=self.dia)
#         dia_entry.grid(column=3, row=2)
        
#         # RPM Output
#         self.sf = StringVar()
#         CTkLabel(master=self, width=40, justify="right", textvariable=self.sf).grid(column=4, row=1, rowspan=2, padx=5, sticky="e")
#         CTkLabel(master=self, text=" Feet per Minute").grid(column=5, row=1, rowspan=2, sticky="w")

#     def calculate(self, *args):
#         try:
#             get_rpm = int(self.rpm.get())
#             get_dia = float(self.dia.get())
#             self.sf.set(round((get_rpm*pi*get_dia)/12))
#         except ValueError:
#             pass

            

