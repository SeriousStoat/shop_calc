#!/usr/bin/python3
# This is the prototype of the Feeds and Speeds Calculator
# It fully functions as a command line application
# I plan to make it part of a bigger GUI application
import math

#Menu Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
welcome = """
+---------------------------------+
|  Welcome to My Shop Calculator  |
+---------------------------------+

What would you like to calculate?
"""

options = {
    1: "-- RPMs (Revolutions per Minute)",
    2: "-- SF (Square Feet per Minute)",
    3: "-- Feed (Inches per Minute)",
    4: "-- Chipload (Inches per Tooth per revolution)",
    "Q": "-- Exit."}

prompt = """
Would you like to make another calculation?
Press 'O' for list of options, or press 'Q' to exit"""

#Get User Input for Class Variables and check if User input is valid ~~~~~~~~~~~~~~
class Get:
    def __init__(self, find, type, message):
        self.find = find
        self.type = type
        self.message = message

    def check(self):
        error = "Error: Enter a valid number."
        while True:
            try:
                self.find = self.type(input(self.message))
            except ValueError:
                print(error)
                continue
            if self.type(self.find) <= 0:
                print(error)
                continue
            else: break
            
#Get Instances
get_dia = Get("dia", float, "Please enter your part Dia: ")
get_sf = Get("sf", int, "Please enter your desired Surface Footage: ")
get_rpm = Get("rpm", int, "Please enter your Spindle RPMs: ")
get_chipload =  Get("cl", float, "Please enter your desired chipload: ")
get_teeth = Get("teeth", int, "Please enter the number of cutting edges (or teeth): ")
get_feed = Get("feed", float, "Please enter your Feedrate: ")

#Calculations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Calc(Get):
    def __init__(self, find, type, message):
        super().__init__(find, type, message)

    def rpm():
        get_sf.check()
        get_dia.check()
        rpm = int((float(get_sf.find)*12)/(math.pi*float(get_dia.find)))
        print("\nSet your spindle RPMs to "+str(rpm)+"rpm")
        
    def sf():
        get_rpm.check()
        get_dia.check()
        sf = int((math.pi*float(get_dia.find)*float(get_rpm.find))/12.0)
        print("\nYour Surface Footage is "+str(sf)+"(square feet per minute)")

    def feed():
        get_rpm.check()
        get_chipload.check()
        get_teeth.check()
        feed = round(float(get_rpm.find)*float(get_chipload.find)*float(get_teeth.find), 2)
        print("\nSet your feed to "+str(feed)+" (inches per minute)")

    def chipload():
        get_rpm.check()
        get_teeth.check()
        get_feed.check()
        cl = round(float(get_feed.find)/((float(get_rpm.find)*float(get_teeth.find))), 4)
        print("\nYour Chip Load is "+str(cl)+" (inches per tooth)")

# Initial Welcome Message #
print(welcome)
for key, value in options.items():
    print(f"{key}: {value}")
#Menu Selections ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:
    select = input("Enter your selection: ")

   # Route Menu Selection to related calculation functions 
    if select == "1":
        Calc.rpm()
    elif select == "2":
        Calc.sf()
    elif select == "3":
        Calc.feed()
    elif select == "4":
        Calc.chipload()     
    elif select.casefold() == "o":
        for key, value in options.items():
            print(f"{key}: {value}")
        continue
    elif select.casefold() == "q":
        print ("\nThank you for using John\'s Shop Calculator!")
        exit()

    # Let User know if they chose an invalid option
    else:
        print("ERROR: Please select a valid option.")
        continue

    print(prompt)
