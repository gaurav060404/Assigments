import sqlite3
import tkinter as tk
from tkinter import messagebox

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
                                noOfBooksIssued INTEGER,
                                enrNo TEXT,
                                mID TEXT)''')
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

class Book:
    def __init__(self, bookID, bookName, price, author, publication):
        self.bookID = bookID
        self.bookName = bookName
        self.price = price
        self.author = author
        self.publication = publication
        db.cursor.execute("INSERT OR IGNORE INTO Book (bookID, bookName, price, author, publication) VALUES (?, ?, ?, ?, ?)",
                          (bookID, bookName, price, author, publication))
        db.conn.commit()

class Member:
    def __init__(self, name, contact, mType, noOfBooksIssued=0, enrNo=None, mID=None):
        self.name = name
        self.contact = contact
        self.mType = mType
        self.noOfBooksIssued = noOfBooksIssued
        self.enrNo = enrNo
        self.mID = mID
        db.cursor.execute("INSERT OR IGNORE INTO Member (name, contact, mType, noOfBooksIssued, enrNo, mID) VALUES (?, ?, ?, ?, ?, ?)",
                          (name, contact, mType, noOfBooksIssued, enrNo, mID))
        db.conn.commit()

class Student(Member):
    def __init__(self, name, contact, enrNo):
        super().__init__(name, contact, "Student", enrNo=enrNo)

class Staff(Member):
    def __init__(self, name, contact, mID):
        super().__init__(name, contact, "Staff", mID=mID)

class Library:
    def add_book(self, bookID, bookName, price, author, publication):
        Book(bookID, bookName, price, author, publication)
        messagebox.showinfo("Success", f"Book '{bookName}' added successfully!")

    def add_member(self, name, contact, mType, enrNo=None, mID=None):
        if mType == "Student":
            Student(name, contact, enrNo)
        elif mType == "Staff":
            Staff(name, contact, mID)
        else:
            Member(name, contact, mType)
        messagebox.showinfo("Success", f"Member '{name}' added successfully!")

library = Library()

# GUI Implementation
root = tk.Tk()
root.title("Library Management System")
root.geometry("400x300")

def add_book_gui():
    def submit():
        library.add_book(int(book_id.get()), book_name.get(), float(price.get()), author.get(), publication.get())
    
    book_window = tk.Toplevel(root)
    book_window.title("Add Book")
    tk.Label(book_window, text="Book ID").pack()
    book_id = tk.Entry(book_window)
    book_id.pack()
    tk.Label(book_window, text="Book Name").pack()
    book_name = tk.Entry(book_window)
    book_name.pack()
    tk.Label(book_window, text="Price").pack()
    price = tk.Entry(book_window)
    price.pack()
    tk.Label(book_window, text="Author").pack()
    author = tk.Entry(book_window)
    author.pack()
    tk.Label(book_window, text="Publication").pack()
    publication = tk.Entry(book_window)
    publication.pack()
    tk.Button(book_window, text="Submit", command=submit).pack()

def add_member_gui():
    def submit():
        library.add_member(name.get(), contact.get(), mType.get(), enrNo.get() if mType.get() == "Student" else None, mID.get() if mType.get() == "Staff" else None)
    
    member_window = tk.Toplevel(root)
    member_window.title("Add Member")
    tk.Label(member_window, text="Name").pack()
    name = tk.Entry(member_window)
    name.pack()
    tk.Label(member_window, text="Contact").pack()
    contact = tk.Entry(member_window)
    contact.pack()
    tk.Label(member_window, text="Member Type (Student/Staff/Regular)").pack()
    mType = tk.Entry(member_window)
    mType.pack()
    tk.Label(member_window, text="Enrollment No (For Students)").pack()
    enrNo = tk.Entry(member_window)
    enrNo.pack()
    tk.Label(member_window, text="Staff ID (For Staff)").pack()
    mID = tk.Entry(member_window)
    mID.pack()
    tk.Button(member_window, text="Submit", command=submit).pack()

tk.Button(root, text="Add Book", command=add_book_gui).pack()
tk.Button(root, text="Add Member", command=add_member_gui).pack()

root.mainloop()

db.close()
