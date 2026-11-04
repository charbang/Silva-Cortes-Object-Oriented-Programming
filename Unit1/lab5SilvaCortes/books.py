class book:
    def __init__(self, id_book, name, author, editorial):
        self.id = id_book
        self.name = name
        self.author = author
        self.editorial = editorial
    def show_book_info(self):
        # True when book is available to borrow
        self.available = True
        # id of user who borrowed the book (None if available)
        self.borrower = None

    def show_book_info(self):
        status = "Available" if self.available else f"Borrowed by {self.borrower}"
        return f"ID: {self.id}\n- {self.name}\n- {self.author}\n- {self.editorial}\n- Status: {status}\n"