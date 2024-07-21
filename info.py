from customtkinter import CTkToplevel, CTkLabel, CTkTextbox, CTkButton

class Info(CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry("640x370+300+100")
        self.title("About - My Shop Calculator")
        self.grid_columnconfigure(0, weight=1)

        CTkLabel(master=self, text='About', font=("Tahoma", 16, "bold")).grid(row=0, column=0, pady=10)
        self.about = CTkTextbox(master=self, width=230)
        self.about.grid(row=1, column=0, padx=10, sticky="nsw")
        self.about._textbox.tag_configure("text", justify="center")
        self.about.insert("0.0",
                            "My Shop Calculator\n"
                            "Version 0.0.4\n"
                            "Created by SeriousStoat\n"
                            "aseriousstoat@pm.me\n"
                            "\n"
                            "Developed with:\n"
                            "Python 3.11.2\n"
                            "CustomTkinter 5.2.2\n"
                            "Pillow 10.4.0")
        self.about._textbox.tag_add("text", "0.0", "end")
        self.about.configure(state="disabled")

        CTkLabel(master=self, text='How To Use', font=("Tahoma", 16, "bold")).grid(row=0, column=1, pady=10)
        self.howto = CTkTextbox(master=self, width=400, height=270, font=("Arial", 14), pady=10, spacing3=10, wrap='word')
        self.howto.grid(row=1, column=1, padx=10)
        self.howto.insert("0.0",
                            "This is a shop aid for machinists.\n"
                            "The calulations are 'adaptive', meaning any calculation that can be "
                            "derived or updated from the selected calculation will be, when a "
                            "'calculate' command is given (ether will a button or the <enter> key).\n"
                            "The <tab> and <shift>+<tab> keys can be used to cycle through entry forms.\n"
                            "If you have any suggestions or requests please send them to my email.\n"
                            "\n"
                            "Thank you for using My Shop Calculator")
        self.howto._textbox.tag_add("text", "0.0", "end")

        def exitwindow():
            self.destroy()

        okay_btn = CTkButton(master=self, text="Okay", width=400, command=exitwindow)
        okay_btn.grid(row=2, column=0, columnspan=2, pady=10)