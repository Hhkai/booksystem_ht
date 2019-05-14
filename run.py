import sys
import utils
import time
from hypertable.thriftclient import *
from hyperthrift.gen.ttypes import *

client = ThriftClient("localhost", 15867)
namespace = client.namespace_open("booksystem")

print "insert books from file 'books.txt'..."
with open('books.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        if len(line) == 4:
            ind, name, author, editor = line[:4]
            utils.insertbook(client, namespace, ind, name, author, editor)
print "successfully inserted"

print "delete book 'B001':"
print "call utils.deletebook()..."
utils.deletebook(client, namespace, "B001")
print "successfully deleted"

print "insert books from file 'students.txt'..."
with open('students.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        if len(line) == 2:
            ind, author = line[:2]
            utils.insertstudent(client, namespace, ind, name)
print "successfully inserted"

print "delete student 'S001':"
print "call utils.deletestudent()..."
utils.deletestudent(client, namespace, "S001")
print "successfully deleted"

print "insert borrows from file 'borrows.txt'..."
with open('borrows.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        if len(line) == 2:
            stu_id, book_id = line[:2]
            utils.insertborrow(client, namespace, stu_id, book_id)
print "successfully inserted"

print "delete borrow 'S002 B002':"
print "call utils.deleteborrow()..."
utils.deleteborrow(client, namespace, "S002", "B002")
print "successfully deleted"

print "show all the books borrowed"
print utils.allborrows(client, namespace)
