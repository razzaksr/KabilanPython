from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from tkinter.ttk import Combobox

from pymysql import *

class View(Tk):
    def hai(self,event):
        #print('entered')
        self.show()
    def hi(self, event):
        print('left')
    def __init__(self):
        Tk.__init__(self)
        self.title('View All Services')
        self.geometry('500x300')
        self.lab=Label(self,text='Viewing Services',font=('Arial',22,BOLD))
        self.lab.grid(row=1,column=10)
        #self.bind('<Enter>',self.hai)
        #self.bind('<Leave>', self.hi)
        #self.show()
        self.combo=Combobox(self,values=['All','Specific'])
        self.combo.bind('<<ComboboxSelected>>',self.which)
        self.combo.grid(row=2,column=0)
    def which(self,event):
        if self.combo.get()=='Specific':
            self.w=Entry(self)
            self.w.grid(row=3,column=0)
            self.but=Button(self,text="submit",command=self.single)
            self.but.grid(row=3,column=2)
        else:
            self.show()
    def single(self):
        self.ha = Entry(self);
        self.ha.insert(END, 'JobNumber');
        self.ha.grid(row=4, column=0)
        self.hb = Entry(self);
        self.hb.insert(END, 'RegistrationNumber');
        self.hb.grid(row=4, column=1)
        self.hc = Entry(self);
        self.hc.insert(END, 'PickedUpDate');
        self.hc.grid(row=4, column=2)
        self.hd = Entry(self);
        self.hd.insert(END, 'CustomerName');
        self.hd.grid(row=4, column=3)
        self.he = Entry(self);
        self.he.insert(END, 'Contact');
        self.he.grid(row=4, column=4)
        self.hf = Entry(self);
        self.hf.insert(END, 'Issues');
        self.hf.grid(row=4, column=5)
        self.hg = Entry(self);
        self.hg.insert(END, 'ExpectedDayToDeliver');
        self.hg.grid(row=4, column=6)
        self.hh = Entry(self);
        self.hh.insert(END, 'Bill amount');
        self.hh.grid(row=4, column=7)
        con = connect(host='localhost', user='root', passwd='', database='kabilan')
        qry = 'select * from jobs where number=' + self.w.get()
        cur = con.cursor()
        cur.execute(qry)
        every = cur.fetchone()

        for each in range(len(every)):
            self.d = Entry(self)
            self.d.insert(END, every[each])
            self.d.grid(row=5, column=each)

    def show(self):
        self.ha=Entry(self);self.ha.insert(END,'JobNumber');self.ha.grid(row=4,column=0)
        self.hb = Entry(self);self.hb.insert(END, 'RegistrationNumber');self.hb.grid(row=4, column=1)
        self.hc = Entry(self);self.hc.insert(END, 'PickedUpDate');self.hc.grid(row=4, column=2)
        self.hd = Entry(self);self.hd.insert(END, 'CustomerName');self.hd.grid(row=4, column=3)
        self.he = Entry(self);self.he.insert(END, 'Contact');self.he.grid(row=4, column=4)
        self.hf = Entry(self);self.hf.insert(END, 'Issues');self.hf.grid(row=4, column=5)
        self.hg = Entry(self);self.hg.insert(END, 'ExpectedDayToDeliver');self.hg.grid(row=4, column=6)
        self.hh = Entry(self);self.hh.insert(END, 'Bill amount');self.hh.grid(row=4, column=7)
        con=connect(host='localhost',user='root',passwd='',database='kabilan')
        qry='select * from jobs'
        cur=con.cursor()
        cur.execute(qry)
        every=cur.fetchall()

        line=5
        for row in every:
            for each in range(len(row)):
                self.d=Entry(self)
                self.d.insert(END,row[each])
                self.d.grid(row=line,column=each)
            '''self.combo=Combobox(self,values=['Edit','Delete'])
            self.combo.grid(row=line,column=8)
            self.act=Button(self,text="Action",command=self.extract(row[0]))
            self.act.grid(row=line,column=9)'''
            #self.combo.bind('<<ComboboxSelected>>', self.extract)
            line+=1

        con.close()
    def extract(self,data):
        print(data)

v=View()
v.mainloop()

'''hai=Tk()
hai.geometry('500x500')
hai.mainloop()'''