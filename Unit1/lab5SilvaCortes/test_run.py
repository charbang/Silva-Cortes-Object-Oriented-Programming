from books import book
from user import user
from library import library

lib = library()
# create sample
b1 = book(1, "Book One", "Author A", "Editorial X")
lib.add_book(b1)
u1 = user("u1", "User One")
lib.add_user(u1)

print('Before borrow:')
lib.show_books()
ok, msg = lib.borrow_book(1, "u1")
print('Borrow attempt:', ok, msg)
print('After borrow:')
lib.show_books()
# try borrow again
ok, msg = lib.borrow_book(1, "u1")
print('Second borrow attempt:', ok, msg)
# return
ok, msg = lib.return_book(1, "u1")
print('Return attempt:', ok, msg)
print('After return:')
lib.show_books()
