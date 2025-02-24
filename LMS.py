import sqlite3

class DatabaseManager:
    def __init__(self, db_name="library.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS librarians (
                id INTEGER PRIMARY KEY,
                name TEXT,
                contact_no TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL,
                author TEXT,
                publication TEXT,
                issued_to INTEGER
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                member_id INTEGER PRIMARY KEY,
                name TEXT,
                contact TEXT,
                member_type TEXT,
                no_of_books_issued INTEGER
            )
        """)
        self.connection.commit()

    def insert_librarian(self, librarian):
        self.cursor.execute(
            "INSERT OR IGNORE INTO librarians (id, name, contact_no) VALUES (?, ?, ?)", 
            (librarian.id, librarian.name, librarian.contact_no)
        )
        self.connection.commit()

    def insert_book(self, book):
        self.cursor.execute(
            "INSERT OR IGNORE INTO books (book_id, name, price, author, publication, issued_to) VALUES (?, ?, ?, ?, ?, ?)", 
            (book.book_id, book.name, book.price, book.author, book.publication, book.issued_to)
        )
        self.connection.commit()

    def insert_member(self, member):
        self.cursor.execute(
            "INSERT OR IGNORE INTO members (member_id, name, contact, member_type, no_of_books_issued) VALUES (?, ?, ?, ?, ?)", 
            (member.member_id, member.get_name(), member.contact, member.member_type, member.no_of_books_issued)
        )
        self.connection.commit()

    def close(self):
        self.connection.close()


class Librarian:
    def __init__(self, id, name, contact_no):
        self.id = id
        self.name = name
        self.contact_no = contact_no

    def update_info(self, name=None, contact_no=None):
        if name:
            self.name = name
        if contact_no:
            self.contact_no = contact_no
        print(f"Librarian {self.id} updated.")
        return 1

    def login(self, uname, password):
        print(f"Librarian {uname} logged in.")
        return True


class Book:
    def __init__(self, book_id, name, price, author, publication):
        self.book_id = book_id
        self.name = name
        self.price = price
        self.author = author
        self.publication = publication
        self.issued_to = None  

    def issue_book(self, member_id):
        if self.issued_to is None:
            self.issued_to = member_id
            print(f"Book '{self.name}' issued to Member {member_id}.")
        else:
            print(f"Book '{self.name}' is already issued.")

    def return_book(self):
        if self.issued_to is not None:
            print(f"Book '{self.name}' returned by Member {self.issued_to}.")
            self.issued_to = None
        else:
            print(f"Book '{self.name}' is not issued to anyone.")

    def update_book(self, name=None, price=None, author=None, publication=None):
        if name:
            self.name = name
        if price:
            self.price = price
        if author:
            self.author = author
        if publication:
            self.publication = publication
        print(f"Book '{self.book_id}' updated.")


class Member:
    def __init__(self, member_id, name, contact, member_type):
        self.member_id = member_id
        self.__name = name      
        self.contact = contact
        self.member_type = member_type
        self.no_of_books_issued = 0

    def get_name(self):
        return self.__name

    def issue_book(self, book):
        if self.no_of_books_issued < 3:  
            book.issue_book(self.member_id)
            self.no_of_books_issued += 1
        else:
            print(f"Member {self.get_name()} has already issued maximum books.")

    def return_book(self, book):
        book.return_book()
        self.no_of_books_issued -= 1

    def update_info(self, name=None, contact=None, member_type=None):
        if name:
            self.__name = name
        if contact:
            self.contact = contact
        if member_type:
            self.member_type = member_type
        print(f"Member {self.member_id} updated.")


class Library:
    def __init__(self, id, name, db):
        self.id = id
        self.name = name
        self.db = db
        self.librarians = []  
        self.books = []
        self.members = []

    def add_librarian(self, librarian):
        self.librarians.append(librarian)
        self.db.insert_librarian(librarian)
        print(f"Librarian {librarian.name} assigned to {self.name} Library.")

    def add_book(self, book):
        self.books.append(book)
        self.db.insert_book(book)
        print(f"Book '{book.name}' added to {self.name} Library.")

    def add_member(self, member):
        self.members.append(member)
        self.db.insert_member(member)
        print(f"Member {member.get_name()} registered in {self.name} Library.")

    def remove_librarian(self, librarian_id):
        self.librarians = [lib for lib in self.librarians if lib.id != librarian_id]
        print(f"Librarian with ID {librarian_id} removed.")

    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.book_id != book_id]
        print(f"Book with ID {book_id} removed.")

    def remove_member(self, member_id):
        self.members = [member for member in self.members if member.member_id != member_id]
        print(f"Member with ID {member_id} removed.")

    def list_books(self):
        print("\nBooks in Library:")
        for book in self.books:
            print(f"- {book.name} (ID: {book.book_id}, Issued: {'Yes' if book.issued_to else 'No'})")

    def list_members(self):
        print("\nMembers in Library:")
        for member in self.members:
            print(f"- {member.get_name()} (ID: {member.member_id}, Type: {member.member_type})")


db = DatabaseManager("lms.db")
library = Library(1, "PIT", db)

librarian1 = Librarian(101, "Gaurav", "9876543210")
librarian2 = Librarian(102, "Skywright", "9876500000")
library.add_librarian(librarian1)
library.add_librarian(librarian2)

book1 = Book(201, "Python Programming", 1500, "John Doe", "TechPress")
book2 = Book(202, "Machine Learning", 700, "Jane Smith", "AI Publications")
library.add_book(book1)
library.add_book(book2)

member1 = Member(301, "Charlie", "9876543211", "Student")
member2 = Member(302, "David", "9876543212", "Staff")
library.add_member(member1)
library.add_member(member2)

library.list_books()
library.list_members()

member1.issue_book(book1)  
member1.issue_book(book2) 
library.list_books()

member1.return_book(book1)  
library.list_books()

db.close()
