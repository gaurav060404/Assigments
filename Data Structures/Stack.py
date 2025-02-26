import tkinter as tk
from tkinter import messagebox

class StackGUI:
    def __init__(self, root, size):
        self.stack = []
        self.size = size
        self.top = -1

        root.title("Stack GUI")

        self.entry = tk.Entry(root, width=20)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        self.push_button = tk.Button(root, text="Push", command=self.push, width=10)
        self.push_button.grid(row=0, column=1, padx=5)

        self.pop_button = tk.Button(root, text="Pop", command=self.pop, width=10)
        self.pop_button.grid(row=1, column=1, padx=5)

        self.peek_button = tk.Button(root, text="Peek", command=self.peek, width=10)
        self.peek_button.grid(row=2, column=1, padx=5)

        self.listbox = tk.Listbox(root, height=10, width=30)
        self.listbox.grid(row=1, column=0, rowspan=3, padx=10, pady=10)

    def push(self):
        val = self.entry.get()
        if not val:
            messagebox.showwarning("Warning", "Please enter a value to push")
            return
        
        if self.top + 1 == self.size:
            messagebox.showerror("Error", "Stack Overflow")
            return

        self.top += 1
        self.stack.append(val)
        self.update_stack_display()
        self.entry.delete(0, tk.END)

    def pop(self):
        if self.top == -1:
            messagebox.showerror("Error", "Stack Underflow")
            return

        popped_value = self.stack.pop()
        self.top -= 1
        self.update_stack_display()
        messagebox.showinfo("Popped", f"Popped element: {popped_value}")

    def peek(self):
        if self.top == -1:
            messagebox.showwarning("Warning", "Stack is empty")
            return
        messagebox.showinfo("Peek", f"Top element: {self.stack[self.top]}")

    def update_stack_display(self):
        self.listbox.delete(0, tk.END)
        for item in reversed(self.stack):
            self.listbox.insert(tk.END, item)


root = tk.Tk()
app = StackGUI(root, size=5) 
root.mainloop()
