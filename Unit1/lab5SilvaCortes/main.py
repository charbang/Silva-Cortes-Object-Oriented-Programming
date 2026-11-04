from books import book
from user import user
from library import library


while True:
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    editorial = input("Enter the editorial of the book: ")
    y = input("Do you want to add another book? (y/n): ")
    id = 1
    book1 = book(id, title, author, editorial)
    id += 1
    if y.lower() != y:
        break


user1 = user("001", "Eli Dorado")
user2 = user("002", "Jesus Calamardo")
lib = library()

lib.add_book(book1)
lib.add_user(user1)
lib.add_user(user2)

print("BOOKS")
lib.show_books()
print("USERS")
lib.show_users()
##THE SYSTEM MOST ALLOW TO REGISTER BOOKS
##THE SYSTEM MUST ALLOW TO REGISTER USERS
##THE SYSTEM MUST MANAGE THE BOOKS BORROW PROCESS (USERS)
##A BOOK THAT HAS ALREADY BEEN BORROWED CANNOT BE BORROWED AGAIN"
##THE SYSTEM MUST ALLOW A BOOK TO BE RETURNED

if __name__ == "__main__":
    # Minimal demo: register one book and show
    lib = library()
    b = book(1, "Demo Book", "Author", "Editorial")
    lib.add_book(b)
    u = user("u1", "Demo User")
    lib.add_user(u)
    print("Books:")
    lib.show_books()
    print("Users:")
    lib.show_users()