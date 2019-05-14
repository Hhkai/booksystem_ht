import sys
import time

'''
try:
    client = ThriftClient("localhost", 15867)
    namespace = client.namespace_open("test")
    
    res = client.hql_query(namespace, "show tables")
    print res
    res = client.hql_query(namespace, "select * from thrift_test")
    print res
    print "================================="
    res = client.hql_query(namespace, 'select * from thrift_test where c1="id1"');
    for cell in res.cells:
	print "-", cell.key.row, type(cell.key.row)
    
    
except:
    print sys.exc_info()
    raise
'''
def insertbook(client, namespace, ind, name, author, editor):
    times = time.strftime('%y-%m-%d %H:%M:%S', time.localtime()) # str
    # print ind, name, author, editor
    res = client.hql_query(namespace, 
            'insert into books values ("%s", "%s", "%s", "%s")' % (times, ind, "id", ind))
    res = client.hql_query(namespace, 
            'insert into books values ("%s", "%s", "%s", "%s")' % (times, ind, "name", name))
    res = client.hql_query(namespace, 
            'insert into books values ("%s", "%s", "%s", "%s")' % (times, ind, "author", author))
    res = client.hql_query(namespace, 
            'insert into books values ("%s", "%s", "%s", "%s")' % (times, ind, "editor", editor))

def findbookbyname(client, namespace, name):
    mess = ''
    res = client.hql_query(namespace, 'select * from books where name="%s"' % name)
    for cell in res.cells:
        row = cell.key.row
        book = client.hql_query(namespace, 'select * from books where row="%s"' % row)
        for i in book.cells:
            mess += str(i.value) + '\t'
        mess += '\n'
    return mess

def findbookbyauthor(client, namespace, author):
    mess = ''
    res = client.hql_query(namespace, 'select * from books where author="%s"' % author)
    for cell in res.cells:
        row = cell.key.row
        book = client.hql_query(namespace, 'select * from books where row="%s"' % row)
        for i in book.cells:
            mess += str(i.value) + '\t'
        mess += '\n'
    return mess

def deletebook(client, namespace, ind):
    res = client.hql_query(namespace, 'delete * from books where row="%s"' % ind)

def insertstudent(client, namespace, ind, name):
    times = time.strftime('%y-%m-%d %H:%M:%S', time.localtime()) # str
    # print ind, name, author, editor
    res = client.hql_query(namespace, 
            'insert into students values ("%s", "%s", "%s", "%s")' % (times, ind, "id", ind))
    res = client.hql_query(namespace, 
            'insert into students values ("%s", "%s", "%s", "%s")' % (times, ind, "name", name))

def deletestudent(client, namespace):
    res = client.hql_query(namespace, 'delete * from students where row="%s"' % ind)

def insertborrow(client, namespace, stu_id, book_id):
    times = time.strftime('%y-%m-%d %H:%M:%S', time.localtime()) # str
    ind = str(time.time())
    # print ind, name, author, editor
    res = client.hql_query(namespace, 
            'insert into borrows values ("%s", "%s", "%s", "%s")' % (times, ind, "stu_id", stu_id))
    res = client.hql_query(namespace, 
            'insert into borrows values ("%s", "%s", "%s", "%s")' % (times, ind, "book_id", book_id))

def deleteborrow(client, namespace, stu_id, book_id):
    res = client.hql_query(namespace, 
            'select * from borrows where stu_id="%s" and book_id="%s"' % (stu_id, bookid))

def allborrows(client, namespace):
    mess = ''
    times = time.strftime('%y-%m-%d %H:%M:%S', time.localtime()) # str
    res = client.hql_query(namespace, 'select * from borrows')
    rows = set()
    for cell in res.cells:
        rows.add(cell.key.row)
    for row in rows:
        borrow = client.hql_query(namespace, 'select * from borrows where row="%s"' % row)
        stu_id, book_id = borrow.cells[:2]
        mess += getstudentname(client, namespace, str(stu_id.value)) + ': ' + getbookname(
                               client, namespace, str(book_id.value))
        mess += '\n'
    return mess

def getstudentname(client, namespace, ind):
    mess = ''
    student = client.hql_query(namespace, 'select * from students where row="%s"' % ind)
    for i in student.cells:
        mess += str(i.value) + '\t'
    return mess
def getbookname(client, namespace, ind):
    mess = ''
    book = client.hql_query(namespace, 'select * from books where row="%s"' % ind)
    for i in book.cells:
        mess += str(i.value) + '\t'
    return mess
