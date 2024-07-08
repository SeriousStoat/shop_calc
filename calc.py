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
        self.calcrpm.grid(column=1, row=1, rowspan=2, pady=5, padx=(5,40))

            # SFM Input
        CTkLabel(master=self.rpm_frame, text="Surface Footage ").grid(column=2, row=1, sticky="e")
        self.rpm_sfm = StringVar()
        self.rpm_sfm_entry = CTkEntry(master=self.rpm_frame, width=50, textvariable=self.rpm_sfm)
        self.rpm_sfm_entry.grid(column=3, row=1, padx=5)

            # Dia Input
        CTkLabel(master=self.rpm_frame, text="Part or Cutter Dia ").grid(column=2, row=2, sticky="e")
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
        self.calcsfm.grid(column=1, row=1, rowspan=2, pady=5, padx=(5,40))

            # RPM Input
        CTkLabel(master=self.sfm_frame, text="RPMs ").grid(column=2, row=1, sticky="e")
        self.sfm_rpm = StringVar()
        self.sfm_rpm_entry = CTkEntry(master=self.sfm_frame, width=50, textvariable=self.sfm_rpm)
        self.sfm_rpm_entry.grid(column=3, row=1, padx=5)

            # Dia Input
        CTkLabel(master=self.sfm_frame, text="Part or Cutter Dia ").grid(column=2, row=2, sticky="e")
        self.sfm_dia = StringVar()
        self.sfm_dia_entry = CTkEntry(master=self.sfm_frame, width=50, textvariable=self.sfm_dia)
        self.sfm_dia_entry.grid(column=3, row=2)
        
            # RPM Output
        self.sfm = StringVar()
        CTkLabel(master=self.sfm_frame, text=">").grid(column=4, row=1, rowspan=2, padx=5, sticky="e")
        CTkLabel(master=self.sfm_frame, width=40, justify="right", textvariable=self.sfm, text_color="orange")\
            .grid(column=5, row=1, rowspan=2, padx=5, sticky="e")
        
        # Feed Frame
        self.feed_frame = CTkFrame(master=self, corner_radius=0)
        self.feed_frame.pack(fill="both", expand=True, pady=5)

            # Calulation Button
        self.calcfeed= CTkButton(master=self.feed_frame, text="Calculate Feed (ipm)", command=self.calcFeed)
        self.calcfeed.grid(column=1, row=1, rowspan=3, pady=5, padx=(5,40))

            # RPM Input
        CTkLabel(master=self.feed_frame, text="RPMs ").grid(column=2, row=1, sticky="e")
        self.feed_rpm = StringVar()
        self.feed_rpm_entry = CTkEntry(master=self.feed_frame, width=50, textvariable=self.feed_rpm)
        self.feed_rpm_entry.grid(column=3, row=1, padx=5)

            # IPR Input
        CTkLabel(master=self.feed_frame, text="IPR ").grid(column=2, row=2, sticky="e")
        self.feed_ipr = StringVar()
        self.feed_ipr_entry = CTkEntry(master=self.feed_frame, width=50, textvariable=self.feed_ipr)
        self.feed_ipr_entry.grid(column=3, row=2, padx=5)

            # Teeth Input                                                       
        CTkLabel(master=self.feed_frame, text="Number of Teeth ").grid(column=2, row=3, sticky="e")
        self.feed_teeth = StringVar()
        self.feed_teeth_entry = CTkEntry(master=self.feed_frame, width=50, textvariable=self.feed_teeth)
        self.feed_teeth_entry.grid(column=3, row=3, padx=5)

            # Feed Output
        self.feed = StringVar()
        CTkLabel(master=self.feed_frame, text="> ").grid(column=4, row=1, rowspan=3, padx=5, sticky="e")
        CTkLabel(master=self.feed_frame, width=40, justify="right", textvariable=self.feed, text_color="orange")\
            .grid(column=5, row=1, rowspan=3, padx=5, sticky="e")
        
        # Chipload Frame
        self.chipload_frame = CTkFrame(master=self, corner_radius=0)
        self.chipload_frame.pack(fill="both", expand=True, pady=5)

            # Calulation Button
        self.calcfeed= CTkButton(master=self.chipload_frame, text="Calculate Feed (ipm)", command=self.calcChip)
        self.calcfeed.grid(column=1, row=1, rowspan=3, pady=5, padx=(5,40))

            # RPM Input
        CTkLabel(master=self.chipload_frame, text="RPMs ").grid(column=2, row=1, sticky="e")
        self.chip_rpm = StringVar()
        self.chip_rpm_entry = CTkEntry(master=self.chipload_frame, width=50, textvariable=self.chip_rpm)
        self.chip_rpm_entry.grid(column=3, row=1, padx=5)

            # Feed Input
        CTkLabel(master=self.chipload_frame, text="Feed(ipm) ").grid(column=2, row=2, sticky="e")
        self.chip_feed = StringVar()
        self.chip_feed_entry = CTkEntry(master=self.chipload_frame, width=50, textvariable=self.chip_feed)
        self.chip_feed_entry.grid(column=3, row=2, padx=5)

            # Teeth Input                                                       
        CTkLabel(master=self.chipload_frame, text="Number of Teeth ").grid(column=2, row=3, sticky="e")
        self.chip_teeth = StringVar()
        self.chip_teeth_entry = CTkEntry(master=self.chipload_frame, width=50, textvariable=self.chip_teeth)
        self.chip_teeth_entry.grid(column=3, row=3, padx=5)

            # Chipload Output
        self.chipload = StringVar()
        CTkLabel(master=self.chipload_frame, text="> ").grid(column=4, row=1, rowspan=3, padx=5, sticky="e")
        CTkLabel(master=self.chipload_frame, width=40, justify="right", textvariable=self.chipload, text_color="orange")\
            .grid(column=5, row=1, rowspan=3, padx=5, sticky="e")

        # Keybinding-Focus Rules
        self.rpm_sfm_entry.bind('<Return>', self.calcRpm)
        self.rpm_dia_entry.bind('<Return>', self.calcRpm)
        self.sfm_rpm_entry.bind('<Return>', self.calcSfm)
        self.sfm_dia_entry.bind('<Return>', self.calcSfm)
        self.feed_rpm_entry.bind('<Return>', self.calcFeed)
        self.feed_ipr_entry.bind('<Return>', self.calcFeed)
        self.feed_teeth_entry.bind('<Return>', self.calcFeed)
        self.chip_rpm_entry.bind('<Return>', self.calcChip)
        self.chip_feed_entry.bind('<Return>', self.calcChip)
        self.chip_teeth_entry.bind('<Return>', self.calcChip)
        self.rpm_sfm_entry.focus()

    # Speed & Feed Calculations
    def calcRpm(self, *args):
        try:
            sfm = int(self.rpm_sfm.get())
            dia = float(self.rpm_dia.get())
            rpm = (round((sfm*12)/(pi*dia)))
            self.rpm.set(f"{rpm} rpm")
            self.sfm_rpm.set(rpm)
            self.feed_rpm.set(rpm)
            self.chip_rpm.set(rpm)
            # Message
            self.msg_frame.label.configure(text=(f"RPMs Calculated @ {rpm} revolutions per minute."), text_color="green")           
        except ValueError:
            self.msg_frame.label.configure(text="RPM Calculation Error : Please enter valid numbers.", text_color="Tomato")
            self.rpm.set("")
        except ZeroDivisionError:
            self.msg_frame.label.configure(text="RPM Calculation Error : Dia cannot be zero.",text_color="Tomato")
            self.rpm.set("")

    def calcSfm(self, *args):
        try:
            rpm = int(self.sfm_rpm.get())
            dia = float(self.sfm_dia.get())
            sfm = (round((rpm*pi*dia)/12))
            self.sfm.set(f"{sfm} sfm")
            # Message
            self.msg_frame.label.configure(text=(f"SFM Calculated @ {sfm} surface feet per minute."), text_color="green")   
        except ValueError:
            self.msg_frame.label.configure(text="SFM Calculation Error : Please enter valid numbers.", text_color="Tomato")
            self.sfm.set("")
    
    def calcFeed(self, *args):
        try:
            rpm = int(self.feed_rpm.get())
            ipr = float(self.feed_ipr.get())
            teeth = int(self.feed_teeth.get())
            feed = round(rpm*ipr*teeth, 2)
            self.feed.set(f"{feed} ipm")
            # Message
            self.msg_frame.label.configure(text=(f"Feed Calculated @ {feed} inches per minute."), text_color="green")   
        except ValueError:
            self.msg_frame.label.configure(text="Feed Calculation Error : Please enter valid numbers.", text_color="Tomato")
            self.sfm.set("")

    def calcChip(self, *args):
        try:
            rpm = int(self.chip_rpm.get())
            feed = float(self.chip_feed.get())
            teeth = int(self.chip_teeth.get())
            chipload = round(feed/(rpm*teeth), 4)
            self.chipload.set(f"{chipload} ipr")
            # Message
            self.msg_frame.label.configure(text=(f"Chipload Calculated @ {feed} inches per revolution."), text_color="green")   
        except ValueError:
            self.msg_frame.label.configure(text="Chipload Calculation Error : Please enter valid numbers.", text_color="Tomato")
            self.sfm.set("")
        except ZeroDivisionError:
            self.msg_frame.label.configure(text="Chipload Calculation Error : rpm and teeth cannot be zero.",text_color="Tomato")
            self.rpm.set("")