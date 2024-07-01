# This program calculates sf + dia to get rpm
# Testing CustomTkInter Module

from customtkinter import *
from math import pi
from msg import MsgBar

class SpeedFeed(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Message Bar
        self.msg_frame = MsgBar(master=self, corner_radius=5, fg_color="#181818", width=600)
        self.msg_frame.pack(fill="both", expand=True, padx=30, pady=5)
        self.msg_frame.label.configure(text="Speeds & Feeds: fill out a form and click 'Calculate' or 'Enter'.", text_color="#e0e0e0")

        # Rpm Frame
        self.rpm_frame = CTkFrame(master=self, corner_radius=0)
        self.rpm_frame.pack(fill="both", expand=True, pady=5)

            # Calculate Button
        self.calcrpm = CTkButton(master=self.rpm_frame, text="Calculate RPMs", command=self.calcRpm)
        self.calcrpm.grid(column=1, row=1, rowspan=2, pady=5, padx=5)

            # SF Input
        CTkLabel(master=self.rpm_frame, text="Surface Footage = ").grid(column=2, row=1, sticky="e")
        self.rpm_sf = StringVar()
        rpm_sf_entry = CTkEntry(master=self.rpm_frame, width=50, textvariable=self.rpm_sf)
        rpm_sf_entry.grid(column=3, row=1, padx=5)

            # Dia Input
        CTkLabel(master=self.rpm_frame, text="Part or Cutter Dia = ").grid(column=2, row=2, padx="40 0", sticky="e")
        self.rpm_dia = StringVar()
        rpm_dia_entry = CTkEntry(master=self.rpm_frame, width=50, textvariable=self.rpm_dia)
        rpm_dia_entry.grid(column=3, row=2)
        
            # RPM Output
        self.rpm = StringVar()
        CTkLabel(master=self.rpm_frame, text=">").grid(column=4, row=1, rowspan=2, padx=5, sticky="e")
        CTkLabel(master=self.rpm_frame, width=40, justify="right", textvariable=self.rpm, text_color="orange")\
            .grid(column=5, row=1, rowspan=2, padx=5, sticky="e")
        
        # Surface Footage Frame
        self.sf_frame = CTkFrame(master=self, corner_radius=0)
        self.sf_frame.pack(fill="both", expand=True, pady=5)

            # Calculate Button
        self.calcsf= CTkButton(master=self.sf_frame, text="Calculate SF", command=self.calcSf)
        self.calcsf.grid(column=1, row=1, rowspan=2, pady=5, padx=5)

            # RPM Input
        CTkLabel(master=self.sf_frame, text="RPMs:").grid(column=2, row=1, sticky="e")
        self.sf_rpm = StringVar()
        sf_rpm_entry = CTkEntry(master=self.sf_frame, width=50, textvariable=self.sf_rpm)
        sf_rpm_entry.grid(column=3, row=1, padx=5)

            # Dia Input
        CTkLabel(master=self.sf_frame, text="Part or Cutter Dia:").grid(column=2, row=2, padx="40 0", sticky="e")
        self.sf_dia = StringVar()
        sf_dia_entry = CTkEntry(master=self.sf_frame, width=50, textvariable=self.sf_dia)
        sf_dia_entry.grid(column=3, row=2)
        
            # RPM Output
        self.sf = StringVar()
        CTkLabel(master=self.sf_frame, text=">").grid(column=4, row=1, rowspan=2, padx=5, sticky="e")
        CTkLabel(master=self.sf_frame, width=40, justify="right", textvariable=self.sf, text_color="orange")\
            .grid(column=5, row=1, rowspan=2, padx=5, sticky="e")

    def calcRpm(self, *args):
        try:
            get_sf = int(self.rpm_sf.get())
            get_dia = float(self.rpm_dia.get())
            give_rpm = (round((get_sf*12)/(pi*get_dia)))
            self.rpm.set(f"{give_rpm} rpm")
            # Message
            self.msg_frame.label.configure(text="RPMs Calculated", text_color="green")           
        except ValueError:
            self.msg_frame.label.configure(text="RPM Calculation Error : Please enter valid numbers.", text_color="Tomato")
            self.rpm.set("")
        except ZeroDivisionError:
            self.msg_frame.label.configure(text="RPM Calculation Error : Cannot divide by zero.",text_color="Tomato")
            self.rpm.set("")

    def calcSf(self, *args):
        try:
            get_rpm = int(self.sf_rpm.get())
            get_dia = float(self.sf_dia.get())
            give_sf = (round((get_rpm*pi*get_dia)/12))
            self.sf.set(f"{give_sf} ft\N{SUPERSCRIPT TWO}/min.")
            # Message
            self.msg_frame.label.configure(text="Surface Footage Calculated", text_color="green")   
        except ValueError:
            self.msg_frame.label.configure(text="SF Calculation Error : Please enter valid numbers.", text_color="Tomato")
            self.sf.set("")
        except ZeroDivisionError:
            self.msg_frame.label.configure(text="SF Calculation Error : Cannot divide by zero.",text_color="Tomato")
            self.sf.set("")
     # This needs to be incorperated into the SpeedsFeeds class   
# class Sf(CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

            

