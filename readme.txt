$cd /opt/hypertable/current/bin
$sudo ./ht-stop-servers.sh
$sudo ./ht-start-all-servers.sh local
$./ht shell
hypertable>create namespace booksystem;
hypertable>use booksystem;
hypertable>create table books (id, name, author, editor);
hypertable>create table students (id, name);
hypertable>create table borrows (stu_id, book_id);

