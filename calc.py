# This program calculates sfm + dia to get rpm
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

        # RPM Frame
        self.rpm_frame = CTkFrame(master=self, corner_radius=0)
        self.rpm_frame.pack(fill="both", expand=True, pady=5)

            # Calculate Button
        self.calcrpm = CTkButton(master=self.rpm_frame, text="Calculate RPMs", command=self.calcRpm)
        self.calcrpm.grid(column=1, row=1, rowspan=2, pady=5, padx=5)

            # SFM Input
        CTkLabel(master=self.rpm_frame, text="Surface Footage = ").grid(column=2, row=1, sticky="e")
        self.rpm_sfm = StringVar()
        self.rpm_sfm_entry = CTkEntry(master=self.rpm_frame, width=50, textvariable=self.rpm_sfm)
        self.rpm_sfm_entry.grid(column=3, row=1, padx=5)

            # Dia Input
        CTkLabel(master=self.rpm_frame, text="Part or Cutter Dia = ").grid(column=2, row=2, padx="40 0", sticky="e")
        self.rpm_dia = StringVar()
        self.rpm_dia_entry = CTkEntry(master=self.rpm_frame, width=50, textvariable=self.rpm_dia)
        self.rpm_dia_entry.grid(column=3, row=2)
        
            # RPM Output
        self.rpm = StringVar()
        CTkLabel(master=self.rpm_frame, text=">").grid(column=4, row=1, rowspan=2, padx=5, sticky="e")
        CTkLabel(master=self.rpm_frame, width=40, justify="right", textvariable=self.rpm, text_color="orange")\
            .grid(column=5, row=1, rowspan=2, padx=5, sticky="e")
        
        # SFM Frame
        self.sfm_frame = CTkFrame(master=self, corner_radius=0)
        self.sfm_frame.pack(fill="both", expand=True, pady=5)

            # Calculate Button
        self.calcsfm= CTkButton(master=self.sfm_frame, text="Calculate SFM", command=self.calcSfm)
        self.calcsfm.grid(column=1, row=1, rowspan=2, pady=5, padx=5)

            # RPM Input
        CTkLabel(master=self.sfm_frame, text="RPMs:").grid(column=2, row=1, sticky="e")
        self.sf_rpm = StringVar()
        self.sfm_rpm_entry = CTkEntry(master=self.sfm_frame, width=50, textvariable=self.sf_rpm)
        self.sfm_rpm_entry.grid(column=3, row=1, padx=5)

            # Dia Input
        CTkLabel(master=self.sfm_frame, text="Part or Cutter Dia:").grid(column=2, row=2, padx="40 0", sticky="e")
        self.sf_dia = StringVar()
        self.sfm_dia_entry = CTkEntry(master=self.sfm_frame, width=50, textvariable=self.sf_dia)
        self.sfm_dia_entry.grid(column=3, row=2)
        
            # RPM Output
        self.sfm = StringVar()
        CTkLabel(master=self.sfm_frame, text=">").grid(column=4, row=1, rowspan=2, padx=5, sticky="e")
        CTkLabel(master=self.sfm_frame, width=40, justify="right", textvariable=self.sfm, text_color="orange")\
            .grid(column=5, row=1, rowspan=2, padx=5, sticky="e")

        # Focus Rules
        self.rpm_sfm_entry.bind('<Return>', self.calcRpm)
        self.rpm_dia_entry.bind('<Return>', self.calcRpm)
        self.sfm_rpm_entry.bind('<Return>', self.calcSfm)
        self.sfm_dia_entry.bind('<Return>', self.calcSfm)
        self.rpm_sfm_entry.focus()

    # Speed & Feed Calculations
    def calcRpm(self, *args):
        try:
            get_sfm = int(self.rpm_sfm.get())
            get_dia = float(self.rpm_dia.get())
            give_rpm = (round((get_sfm*12)/(pi*get_dia)))
            self.rpm.set(f"{give_rpm} rpm")
            # Message
            self.msg_frame.label.configure(text="RPMs Calculated", text_color="green")           
        except ValueError:
            self.msg_frame.label.configure(text="RPM Calculation Error : Please enter valid numbers.", text_color="Tomato")
            self.rpm.set("")
        except ZeroDivisionError:
            self.msg_frame.label.configure(text="RPM Calculation Error : Cannot divide by zero.",text_color="Tomato")
            self.rpm.set("")

    def calcSfm(self, *args):
        try:
            get_rpm = int(self.sf_rpm.get())
            get_dia = float(self.sf_dia.get())
            give_sfm = (round((get_rpm*pi*get_dia)/12))
            self.sfm.set(f"{give_sfm} sfm")
            # Message
            self.msg_frame.label.configure(text="SFM Calculated", text_color="green")   
        except ValueError:
            self.msg_frame.label.configure(text="SFM Calculation Error : Please enter valid numbers.", text_color="Tomato")
            self.sfm.set("")
        except ZeroDivisionError:
            self.msg_frame.label.configure(text="SFM Calculation Error : Cannot divide by zero.",text_color="Tomato")
            self.sfm.set("")