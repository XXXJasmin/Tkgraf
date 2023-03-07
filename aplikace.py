import tkinter as tk
import pylab as pl
from pylab import pi

class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if "textvariable" not in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

class Application(tk.Tk):
    name = "Vyber soubor"
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit)



    def __init__(self):
        super().__init__(className=self.name)
        self.bind("<Escape>", self.quit)
        self.entry = MyEntry(self)
        self.entry.pack(side="top", fill="x")


        self.frame1=tk.Frame(self)
        self.frame1.pack(fill="both")


        self.button1=tk.Button(self.frame1, text="Vyber soubor")
        self.button1.pack(side="top", ipadx=20, ipady=5)
        self.button1.bind("<ButtonRelease-1>", self.file)

        self.button2=tk.Button(self.frame1, text="Ukaž")
        self.button2.pack(side="top", ipadx=20, ipady=5)
        self.button2.bind("<ButtonRelease-1>", self.show)

        self.button3=tk.Button(self.frame1, text="zavřít")
        self.button3.pack(side="bottom", ipadx=20, ipady=5)
        self.button3.bind("<ButtonRelease-1>", self.quit)

    def onclick(self, event:tk.Event):
        print(self.frame1.get("anchor"))
        print(self.frame1.get("active"))
        print(self.frame1.curselection())

    def file(self):
        if self.button1 == self.onclick:

    def show(self):

    def quit(self):
