class library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def find_book(self, book_id):
        for b in self.books:
            if str(b.id) == str(book_id):
                return b
        return None

    def find_user(self, user_id):
        for u in self.users:
            if str(u.id) == str(user_id):
                return u
        return None

    def borrow_book(self, book_id, user_id):
        b = self.find_book(book_id)
        if not b:
            return False, "Book not found"
        if not b.available:
            return False, "Book already borrowed"
        u = self.find_user(user_id)
        if not u:
            return False, "User not found"
        b.available = False
        b.borrower = u.id
        u.borrowed.append(b.id)
        return True, "Book borrowed"

    def return_book(self, book_id, user_id):
        b = self.find_book(book_id)
        if not b:
            return False, "Book not found"
        if b.available:
            return False, "Book was not borrowed"
        if str(b.borrower) != str(user_id):
            return False, "This user did not borrow the book"
        u = self.find_user(user_id)
        if not u:
            return False, "User not found"
        b.available = True
        b.borrower = None
        if b.id in u.borrowed:
            u.borrowed.remove(b.id)
        return True, "Book returned"

    def show_books(self):
        for book in self.books:
            print(book.show_book_info())

    def show_users(self):
        for user in self.users:
            print(user.show_user_info())
    