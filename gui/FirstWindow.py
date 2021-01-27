from tkinter import *
from tkinter import messagebox
from tkinter.font import Font, BOLD


class Mine(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("400x200")
        self.title("Sasi kumar and kabilan")
        self.lab1=Label(self,text='Greetings from Zealous',fg='blue',bg='yellow',font=('Arial',22,BOLD))
        self.lab2 = Label(self, text='Python GUI Training', fg='blue', bg='yellow', font=('Arial', 22, BOLD))
        #self.lab1.pack(side=TOP)
        self.lab1.grid(row=10,column=20)
        self.lab2.grid(row=40,column=100)
        messagebox.showinfo("Info","Window Opened")

m=Mine()
m.mainloop()