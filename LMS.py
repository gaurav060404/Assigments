import sqlite3

# usecases
# model 
# design


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Librarian (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                contactNo TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Book (
                                bookID INTEGER PRIMARY KEY,
                                bookName TEXT,
                                price REAL,
                                author TEXT,
                                publication TEXT,
                                issued_to TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Member (
                                name TEXT PRIMARY KEY,
                                contact TEXT,
                                mType TEXT,
                                noOfBooksIssued INTEGER)''')
        self.conn.commit()

    def close(self):
        self.conn.close()

db = Database()

class Librarian:
    def __init__(self, id, name, contactNo):
        self.id = id
        self.name = name
        self.contactNo = contactNo
        db.cursor.execute("INSERT OR IGNORE INTO Librarian (id, name, contactNo) VALUES (?, ?, ?)", (id, name, contactNo))
        db.conn.commit()

    def updateInfo(self, name=None, contactNo=None):
        if name:
            db.cursor.execute("UPDATE Librarian SET name=? WHERE id=?", (name, self.id))
            self.name = name
        if contactNo:
            db.cursor.execute("UPDATE Librarian SET contactNo=? WHERE id=?", (contactNo, self.id))
            self.contactNo = contactNo
        db.conn.commit()

    def login(self, uname, password):
        return uname == self.name and password == "admin123"

class Book:
    def __init__(self, bookID, bookName, price, author, publication):
        self.bookID = bookID
        self.bookName = bookName
        self.price = price
        self.author = author
        self.publication = publication
        self.issued_to = None
        db.cursor.execute("INSERT OR IGNORE INTO Book (bookID, bookName, price, author, publication) VALUES (?, ?, ?, ?, ?)",
                          (bookID, bookName, price, author, publication))
        db.conn.commit()

    def updateBook(self, bookName=None, price=None, author=None, publication=None):
        if bookName:
            db.cursor.execute("UPDATE Book SET bookName=? WHERE bookID=?", (bookName, self.bookID))
        if price:
            db.cursor.execute("UPDATE Book SET price=? WHERE bookID=?", (price, self.bookID))
        if author:
            db.cursor.execute("UPDATE Book SET author=? WHERE bookID=?", (author, self.bookID))
        if publication:
            db.cursor.execute("UPDATE Book SET publication=? WHERE bookID=?", (publication, self.bookID))
        db.conn.commit()

class Member:
    def __init__(self, name, contact, mType, noOfBooksIssued=0):
        self.name = name
        self.contact = contact
        self.mType = mType
        self.noOfBooksIssued = noOfBooksIssued
        db.cursor.execute("INSERT OR IGNORE INTO Member (name, contact, mType, noOfBooksIssued) VALUES (?, ?, ?, ?)",
                          (name, contact, mType, noOfBooksIssued))
        db.conn.commit()

    def updateMember(self, name=None, contact=None):
        if name:
            db.cursor.execute("UPDATE Member SET name=? WHERE name=?", (name, self.name))
            self.name = name
        if contact:
            db.cursor.execute("UPDATE Member SET contact=? WHERE name=?", (contact, self.name))
            self.contact = contact
        db.conn.commit()

class Staff(Member):
    def __init__(self, mID, name, contact):
        super().__init__(name, contact, "Staff")
        self.mID = mID

class Student(Member):
    def __init__(self, enrNo, name, contact):
        super().__init__(name, contact, "Student")
        self.enrNo = enrNo

    def payFine(self, amount):
        print(f"Student {self.name} paid a fine of {amount}.")

class Library:
    def __init__(self, id,name):
        self.id = id
        self.name = name
        self.db = db

    def add_book(self, bookID, bookName, price, author, publication):
        Book(bookID, bookName, price, author, publication)
        print(f"Book '{bookName}' added to the library.")

    def remove_book(self, bookID):
        db.cursor.execute("DELETE FROM Book WHERE bookID=?", (bookID,))
        db.conn.commit()
        print(f"Book with ID {bookID} removed from the library.")

    def add_member(self, name, contact, mType):
        Member(name, contact, mType)
        print(f"Member '{name}' added to the library.")

    def remove_member(self, name):
        db.cursor.execute("DELETE FROM Member WHERE name=?", (name,))
        db.conn.commit()
        print(f"Member '{name}' removed from the library.")

    def issue_book(self, bookID, memberName):
        db.cursor.execute("SELECT * FROM Book WHERE bookID=?", (bookID,))
        book_data = db.cursor.fetchone()
        
        if book_data and book_data[5] is None:  
            db.cursor.execute("UPDATE Book SET issued_to=? WHERE bookID=?", (memberName, bookID))
            db.cursor.execute("UPDATE Member SET noOfBooksIssued=noOfBooksIssued+1 WHERE name=?", (memberName,))
            db.conn.commit()
            print(f"Book '{book_data[1]}' issued to {memberName}.")
        else:
            print("Book is already issued or does not exist.")

    def return_book(self, bookID, memberName):
        db.cursor.execute("SELECT * FROM Book WHERE bookID=?", (bookID,))
        book_data = db.cursor.fetchone()
        
        if book_data and book_data[5] == memberName:
            db.cursor.execute("UPDATE Book SET issued_to=NULL WHERE bookID=?", (bookID,))
            db.cursor.execute("UPDATE Member SET noOfBooksIssued=noOfBooksIssued-1 WHERE name=?", (memberName,))
            db.conn.commit()
            print(f"Book '{book_data[1]}' returned by {memberName}.")
        else:
            print("This book was not issued to this member.")

library = Library(12522, "PIT Library")
librarian = Librarian(1, "Gaurav", "1234567890")
    
print("=== Add Books ===")
n_books = int(input("How many books would you like to add? "))
for _ in range(n_books):
    bookID = int(input("Enter Book ID: "))
    bookName = input("Enter Book Name: ")
    price = float(input("Enter Book Price: "))
    author = input("Enter Author: ")
    publication = input("Enter Publication: ")
    library.add_book(bookID, bookName, price, author, publication)
    
print("\n=== Add Members ===")
n_members = int(input("How many members would you like to add? "))
for _ in range(n_members):
    name = input("Enter Member Name: ")
    contact = input("Enter Member Contact: ")
    mType = input("Enter Member Type (Regular/Staff/Student): ")
    library.add_member(name, contact, mType)
    
print("\n=== Issue a Book ===")
bookID_issue = int(input("Enter the Book ID to issue: "))
memberForIssue = input("Enter the Member Name to whom the book should be issued: ")
library.issue_book(bookID_issue, memberForIssue)
    
print("\n=== Return a Book ===")
bookID_return = int(input("Enter the Book ID to return: "))
memberForReturn = input("Enter the Member Name returning the book: ")
library.return_book(bookID_return, memberForReturn)
    
print("\n=== Remove a Member ===")
memberToRemove = input("Enter the Member Name to remove from the library: ")
library.remove_member(memberToRemove)


# library = Library(12522,"PIT Library")

# librarian = Librarian(1, "Gaurav", "1234567890")

# library.add_book(101, "Introduction to Python", 250, "John Doe", "Tech Press")
# library.add_book(102, "Advanced Databases", 300, "Jane Doe", "DataPub")

# library.add_member("Jinshi", "9876543210", "Regular")
# library.add_member("Charlie", "0123456789", "Staff")
# library.add_member("David", "1112223333", "Student")

# print("\nIssuing book to member:")
# library.issue_book(101, "Jinshi")

# print("\nReturning book from member:")
# library.return_book(101, "Jinshi")

# student1 = Student("ENR001", "David", "1112223333")
# student1.payFine(50)

# print("\nUpdating member contact info:")
# library.remove_member("Charlie") 
