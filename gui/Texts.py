from tkinter import *
from tkinter import messagebox


class Hold(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("500x300")
        self.title("Text boxes")
        self.lab=Label(self,text="Text Box Demo")
        #self.lab.pack()
        self.lab.grid(row=1,column=5)
        self.alpha=Entry(self)
        self.beta = Entry(self)
        #self.alpha.pack()
        self.alpha.grid(row=5,column=40)
        #self.beta.pack()
        self.beta.grid(row=8,column=40)
        self.bu=Button(self,text="Submit",fg='black',bg='yellow',command=self.hello)
        self.bu.grid(row=10,column=40)
    def hello(self):
        #messagebox.showinfo("Information","Text are: "+self.alpha.get()+self.beta.get())
        self.lab.configure(text=self.alpha.get()+self.beta.get())

h=Hold()
h.mainloop()