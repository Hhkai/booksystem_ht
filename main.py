import sys
import utils
import time
from hypertable.thriftclient import *
from hyperthrift.gen.ttypes import *

welcome = '''

-----------------------------------------------

   welcome to library management system ~ 

-----------------------------------------------
                              hhk ysj tjr
-----------------------------------------------
'''

helpmessage = '''
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

print welcome
print helpmessage
print "You can type `help' to show these messages." 

client = ThriftClient("localhost", 15867)
namespace = client.namespace_open("booksystem")

while True:
    # print time.strftime('%y-%m-%d %H:%M:%S', time.localtime()), type(time.strftime('%y-%m-%d %H:%M:%S', time.localtime()))
    # res = client.hql_query(namespace, 'select * from books')
    # print res
    a = raw_input(">:")
    if a == '1':
        r = raw_input("input id, name, author, editor(split by blank):\n")
        r = r.split()
        utils.insertbook(client, namespace, *r)
    if a == '2':
        r = raw_input("input book name:\n")
        mess = utils.findbookbyname(client, namespace, r)
        print mess
    if a == '3':
        r = raw_input("input author:\n")
        mess = utils.findbookbyname(client, namespace, r)
        print mess
    if a == '4':
        r = raw_input("input book id:\n")
        utils.deletebook(client, namespace, r)
    if a == '5':
        r = raw_input("input id, name(split by blank):\n")
        r = r.split()
        utils.insertstudent(client, namespace, *r)
    if a == '6':
        r = raw_input("input student id:\n")
        utils.deletestudent(client, namespace, r)
    if a == '7':
        r = raw_input("input stu_id, book_id(split by blank):\n")
        r = r.split()
        utils.insertborrow(client, namespace, *r)
    if a == '8':
        r = raw_input("input stu_id, book_id(split by blank):\n")
        r = r.split()
        utils.deleteborrow(client, namespace, *r)
    if a == '9':
        mess = utils.allborrows(client, namespace)
        print mess
    if a == 'x':
        break
    if a == 'help':
        print helpmessage
