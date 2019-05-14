#coding:utf-8
from Tkinter import *
import time
import ScrolledText
import utils
from hypertable.thriftclient import *
from hyperthrift.gen.ttypes import *

class App:
    def __init__(self, master, client, namespace):
        self.client = client
        self.namespace = namespace
        self.welcome = '''
-----------------------------------------------

   welcome to library management system ~ 

-----------------------------------------------
                              hhk ysj tjr
-----------------------------------------------
'''
        self.help = '''
1: insert a book (id, name, author, editor)
2: find books by name
3: find books by author
4: delete a book
5: register a student (id, name)
6: delete a student
7: borrow a book (stu_id, book_id)
8: send back a book (stu_id, book_id)
9: show books borrowed
x: exit
'''
        self.sline = '-----------------------------------------------\n'
        master.geometry("800x600")
        frame1 = Frame(master)
        frame1.pack()
        frame = Frame(master)
        frame.pack()
        Button(frame, text="1",command=lambda: self.callback('1') , width = 5).grid(row=0,column=0)
        Button(frame, text="2",command=lambda: self.callback('2') , width = 5).grid(row=0,column=1)
        Button(frame, text="3",command=lambda: self.callback('3') , width = 5).grid(row=0,column=2)
        Button(frame, text="4",command=lambda: self.callback('4') , width = 5).grid(row=0,column=3)
        Button(frame, text="5",command=lambda: self.callback('5') , width = 5).grid(row=0,column=4)
        Button(frame, text="6",command=lambda: self.callback('6') , width = 5).grid(row=0,column=5)
        Button(frame, text="7",command=lambda: self.callback('7') , width = 5).grid(row=0,column=6)
        Button(frame, text="8",command=lambda: self.callback('8') , width = 5).grid(row=0,column=7)
        Button(frame, text="9",command=lambda: self.callback('9') , width = 5).grid(row=0,column=8)
        Button(frame, text="x",command=lambda: self.callback('x') , width = 10).grid(row=0,column=9)
        
        self.e = ScrolledText.ScrolledText(frame1, width = 80, height = 27)
        self.e.pack(padx=5)
        
        
        w1 = Label(frame1,text="input text here: ")
        w1.pack()
        b = Button(frame1, text="confirm",command=self.submit , width = 10)
        b.pack(side=RIGHT)
        v = StringVar()
        e1 = Entry(frame1, textvariable=v, width = 40)
        v.set("")
        self.inputw = e1
        self.v = v
        e1.pack()
        ##
        self.e.insert(0.0, self.welcome)
        self.e.insert("end", self.help)
        self.e.insert("end", "click a button now ~\n")
        self.e.insert("end", self.sline)
        self.e.config(state="disabled")
        #
        self.flag = 0
    def outputln(self, s):
        self.e.config(state="normal")
        self.e.insert("end", s)
        self.e.see("end")
        self.e.config(state="disabled")
    def submit(self):
        r = self.inputw.get()
        self.outputln("your input: " + r + '\n')
        self.inputw.delete(0, "end")
        r = r.split()
        a = self.flag
        mess = "no operation! ^\n"
        if a == '1':
            mess = utils.insertbook(client, namespace, *r)
        if a == '2':
            mess = utils.findbookbyname(client, namespace, *r)
        if a == '3':
            mess = utils.findbookbyauthor(client, namespace, *r)
        if a == '4':
            mess = utils.deletebook(client, namespace, *r)
        if a == '5':
            mess = utils.insertstudent(client, namespace, *r)
        if a == '6':
            mess = utils.deletestudent(client, namespace, *r)
        if a == '7':
            mess = utils.insertborrow(client, namespace, *r)
        if a == '8':
            mess = utils.deleteborrow(client, namespace, *r)
        self.outputln(mess)
        self.outputln(self.sline)
    def callback(self, a):
        self.flag = a
        if a == '1':
            self.outputln("input id, name, author, editor(split by blank):\n")
        if a == '2':
            self.outputln("input book name:\n")
        if a == '3':
            self.outputln("input author:\n")
        if a == '4':
            self.outputln("input book id:\n")
        if a == '5':
            self.outputln("input id, name(split by blank):\n")
        if a == '6':
            self.outputln("input student id:\n")
        if a == '7':
            self.outputln("input stu_id, book_id(split by blank):\n")
        if a == '8':
            self.outputln("input stu_id, book_id(split by blank):\n")
        if a == '9':
            mess = utils.allborrows(self.client, self.namespace)
            self.outputln("all books borrowed\n")
            self.outputln(mess)
            self.outputln(self.sline)
        if a == 'x':
            exit()
if __name__ == "__main__":
    root = Tk(className = "book management system")
    client = ThriftClient("localhost", 15867)
    namespace = client.namespace_open("booksystem")
    app = App(root, client, namespace)
    root.mainloop()
