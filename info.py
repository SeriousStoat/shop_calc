from customtkinter import CTkToplevel, CTkLabel, CTkTextbox

class Info(CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry("700x300+300+100")
        self.title("About")
        self.grid_columnconfigure(0, weight=1)

        CTkLabel(master=self, text='About', font=("Tahoma", 16, "bold")).grid(row=0, column=0, pady=10)
        self.about = CTkTextbox(master=self, width=230)
        self.about.grid(row=1, column=0, padx=10)
        self.about._textbox.tag_configure("text", justify="center")
        self.about.insert("0.0",
                            "My Shop Calculator\n"
                            "Version 0.0.8\n"
                            "Created by SeriousStoat\n"
                            "aseriousstoat@pm.me\n"
                            "\n"
                            "Made using\n"
                            "Python 3.11.2\n"
                            "CustomTkinter 5.2.2\n"
                            "Pillow 10.4.0")
        self.about._textbox.tag_add("text", "0.0", "end")
        self.about.configure(state="disabled")

        CTkLabel(master=self, text='How To Use', font=("Tahoma", 16, "bold")).grid(row=0, column=1, pady=10)
        self.howto = CTkTextbox(master=self, width=500)
        self.howto.grid(row=1, column=1, padx=10)
        self.howto.insert("0.0",
                            "My Shop Calculator is a shop aid for machinists.\n")
        self.howto._textbox.tag_add("text", "0.0", "end")     