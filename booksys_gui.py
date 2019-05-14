#coding:utf-8
from Tkinter import *
import time

def cacl(input_str):
    if "x" in input_str:
        ret = input_str.split("x")
        return int(ret[0]) * int(ret[1])
    return 999
def callback(n):
    print n
def callback1(n):
    print n
class App:
    def __init__(self, master):
        master.geometry("800x600")
        frame1 = Frame(master)
        frame1.pack()
        frame = Frame(master)
        frame.pack()
        # Button(frame, text="1",command=lambda: callback(1) ).grid(row=0,column=0)
        Button(frame, text="1",command=self.callback(1) , width = 10).grid(row=0,column=0)
        Button(frame, text="2",command=self.callback(2) , width = 10).grid(row=0,column=1)
        Button(frame, text="3",command=self.callback(3) , width = 10).grid(row=0,column=2)
        Button(frame, text="4",command=self.callback(4) , width = 10).grid(row=0,column=3)
        Button(frame, text="5",command=self.callback(5) , width = 10).grid(row=0,column=4)
        Button(frame, text="6",command=self.callback(6) , width = 10).grid(row=0,column=5)
        Button(frame, text="7",command=self.callback(7) , width = 10).grid(row=0,column=6)
        Button(frame, text="8",command=self.callback(8) , width = 10).grid(row=0,column=7)
        Button(frame, text="9",command=self.callback(9) , width = 10).grid(row=0,column=8)
        Button(frame, text="0",command=self.say_hi , width = 10).grid(row=0,column=9)
        w = Label(frame1,text="output")
        w.pack()
        
        self.e = Text(frame1, width = 80)
        self.e.pack(padx=5)
        
        
        w1 = Label(frame1,text="input")
        w1.pack()
        b = Button(frame1, text="confirm",command=self.submit , width = 10)
        b.pack(side=RIGHT)
        v = StringVar()
        e1 = Entry(frame1, textvariable=v)
        v.set("")
        self.inputw = e1
        self.v = v
        e1.pack()
        ##
        self.e.insert(0.0, '''sdfkjskdfjsdlfjsdkf''')
        self.e.config(state="disabled")
    def say_hi(self):
        print "hi there, everyone!",self.e.get("0.0", "end")
        input_str = self.e.get()
        self.v.set(cacl(input_str))
    def callback(self, x):
        print x
    def submit(self):
        print self.inputw.get()
root = Tk(className = "book management system")
app = App(root)
root.mainloop()