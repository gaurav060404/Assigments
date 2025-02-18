import sqlite3
import tkinter as tk
from tkinter import messagebox
import hashlib

class EmptyFieldError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("300x250")

        self.create_db()

        tk.Label(root, text="Username:").pack(pady=5)
        self.username_input = tk.Entry(root)
        self.username_input.pack(pady=5)

        tk.Label(root, text="Password:").pack(pady=5)
        self.password_input = tk.Entry(root, show="*")
        self.password_input.pack(pady=5)

        tk.Button(root, text="Login", command=self.login).pack(pady=10)
        tk.Button(root, text="Register", command=self.register).pack(pady=5)

    def create_db(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        conn.commit()

        # Default = username: admin , password: admin123  
        cursor.execute("SELECT * FROM users WHERE username = ?", ("admin",))
        if not cursor.fetchone():
            hashed_password = hashlib.sha256("admin123".encode()).hexdigest()
            cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", ("admin", hashed_password))
            conn.commit()

        conn.close()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        try:
            username = self.username_input.get().strip()
            password = self.password_input.get().strip()

            if not username or not password:
                raise EmptyFieldError("Both fields must be filled.")

            hashed_password = self.hash_password(password)

            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
            user = cursor.fetchone()
            conn.close()

            if user:
                messagebox.showinfo("Success", "Login Successful!")
                self.root.destroy() 
            else:
                raise InvalidCredentialsError("Invalid Username or Password.")

        except EmptyFieldError as e:
            messagebox.showwarning("Input Error", str(e))
        except InvalidCredentialsError as e:
            messagebox.showwarning("Login Error", str(e))

    def register(self):
        try:
            username = self.username_input.get().strip()
            password = self.password_input.get().strip()

            if not username or not password:
                raise EmptyFieldError("Both fields must be filled.")

            hashed_password = self.hash_password(password)

            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "User registered successfully!")

        except sqlite3.IntegrityError:
            messagebox.showwarning("Registration Error", "Username already exists!")
        except EmptyFieldError as e:
            messagebox.showwarning("Input Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    LoginSystem(root)
    root.mainloop()
