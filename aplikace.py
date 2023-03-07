import tkinter as tk
import pylab as pl
from tkinter import messagebox
from tkinter import filedialog

class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        

class Application(tk.Tk):
    name = "Vyber soubor"
    
    def __init__(self):
        super().__init__(className=self.name)
        self.bind("<Escape>", self.quit)
        self.label = tk.Label(self, text = "---")
        self.label.pack()


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
        
    def file(self, event= None):
        self.filename = filedialog.askopenfilename()
        self.label.config(text=self.filename)

    def show(self, event=None):
        x = []
        y = []

        with open(self.filename,"r") as s:
            while True:
                radek = s.readline()
                if radek == "":
                    break
                linesplit = radek.split()
                if len(linesplit) == 2:
                    a,b = radek.split()
                    x.append(float(a))
                    y.append(float(b))
            pl.plot(x,y)
            pl.grid(1)
            pl.show()
    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()
