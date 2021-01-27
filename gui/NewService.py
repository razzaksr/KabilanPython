from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD, ITALIC

from pymysql import *


class Insert(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("500x300")
        self.title('New Service Job')
        f=('Arial',15,ITALIC)
        self.head=Label(self,text='Garriage Service Log',font=('Arial',20,BOLD))
        self.head.grid(row=1,column=50)
        self.alab=Label(self,text='Vehicle Registration number',font=f)
        self.alab.grid(row=2,column=4)
        self.a=Entry(self)
        self.a.grid(row=2,column=40)
        self.blab = Label(self, text='Vehicle Log date(YYYY-MM-DD)', font=f)
        self.blab.grid(row=3, column=4)
        self.b = Entry(self)
        self.b.grid(row=3, column=40)
        self.clab = Label(self, text='Vehicle Owner name', font=f)
        self.clab.grid(row=4, column=4)
        self.c = Entry(self)
        self.c.grid(row=4, column=40)
        self.dlab = Label(self, text='Vehicle Owner contact', font=f)
        self.dlab.grid(row=5, column=4)
        self.d = Entry(self)
        self.d.grid(row=5, column=40)
        self.elab = Label(self, text='Vehicle Issues', font=f)
        self.elab.grid(row=6, column=4)
        self.e = Entry(self)
        self.e.grid(row=6, column=40)
        self.flab = Label(self, text='Vehicle Delivery expected in Days', font=f)
        self.flab.grid(row=7, column=4)
        self.f = Entry(self)
        self.f.grid(row=7, column=40)
        self.glab = Label(self, text='Vehicle Service Budget', font=f)
        self.glab.grid(row=8, column=4)
        self.g = Entry(self)
        self.g.grid(row=8, column=40)
        self.bu=Button(self,text='Add to Log',command=self.ins)
        self.bu.grid(row=9,column=80)
        self.bu = Button(self, text='Clear', command=self.clear)
        self.bu.grid(row=9, column=160)
    def ins(self):
        con = connect(host='localhost', database='kabilan', user='root', passwd='')
        qry = """insert into jobs(regnum,pick_date,cust_name,cust_contact,issues,expected,exp_bill) values('%s','%s','%s',%d,'%s',%d,%f)""" % \
              (self.a.get(), self.b.get(), self.c.get(), int(self.d.get()), self.e.get(), int(self.f.get()), float(self.g.get()))
        cur = con.cursor()
        ack = cur.execute(qry)
        con.autocommit(True)
        if ack != 0:
            messagebox.showinfo("ack", "vehicle added into logs")
            self.clear()
        else:
            messagebox.showinfo("ack", "vehicle can't added into logs")
    def clear(self):
        clean = StringVar("")



i=Insert()
i.mainloop()