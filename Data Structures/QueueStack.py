import tkinter as tk
from tkinter import messagebox

class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.stack = []

    def push(self, val):
        if self.top + 1 == self.size:
            messagebox.showerror("Error", "Stack Overflow")
            return
        self.stack.append(val)
        self.top += 1

    def pop(self):
        if self.top == -1:
            messagebox.showerror("Error", "Stack Underflow")
            return None
        ele = self.stack.pop()
        self.top -= 1
        return ele

    def peek(self):
        if self.top == -1:
            messagebox.showwarning("Warning", "Stack is empty")
            return None
        return self.stack[self.top]

    def printStack(self):
        return self.stack

class StackQueue:
    def __init__(self, root, size):
        self.size = size
        self.stack1 = []
        self.stack2 = []
        
        root.title("Stack and Queue Visualization")
        
        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.enqueue_entry = tk.Entry(root, width=20)
        self.enqueue_entry.grid(row=1, column=0, padx=10, pady=10)
        
        self.enqueue_button = tk.Button(root, text="Enqueue", command=self.enqueue, width=10)
        self.enqueue_button.grid(row=1, column=1, padx=5)
        
        self.dequeue_button = tk.Button(root, text="Dequeue", command=self.dequeue, width=10)
        self.dequeue_button.grid(row=2, column=1, padx=5)
        
        self.update_display()
    
    def enqueue(self):
        val = self.enqueue_entry.get()
        if not val:
            messagebox.showwarning("Warning", "Please enter a value to enqueue")
            return
        if len(self.stack1) == self.size:
            messagebox.showerror("Error", "Queue Overflow")
            return
        self.stack1.append(val)
        self.stack2.insert(0, val)
        self.update_display()
        self.enqueue_entry.delete(0, tk.END)
    
    def dequeue(self):
        if len(self.stack1) == 0:
            messagebox.showerror("Error", "Queue Underflow")
            return
        ele = self.stack1.pop(0)
        self.stack2.pop()
        messagebox.showinfo("Dequeued", f"Dequeued element: {ele}")
        self.update_display()
    
    def update_display(self):
        self.canvas.delete("all")
        x_start = 50
        y_start_queue = 50
        y_start_stack = 150
        box_width = 60
        box_height = 30
        
        self.canvas.create_text(200, 30, text="Queue", font=("Arial", 14, "bold"))
        for index, item in enumerate(self.stack1):
            self.canvas.create_rectangle(
                x_start + index * box_width, y_start_queue, x_start + (index + 1) * box_width, y_start_queue + box_height,
                fill="lightblue", outline="black"
            )
            self.canvas.create_text(
                x_start + index * box_width + box_width // 2, y_start_queue + box_height // 2,
                text=str(item), font=("Arial", 12, "bold")
            )
        
        self.canvas.create_text(200, 130, text="Stack", font=("Arial", 14, "bold"))
        for index, item in enumerate(self.stack2):
            self.canvas.create_rectangle(
                x_start, y_start_stack - index * box_height, x_start + box_width, y_start_stack - (index - 1) * box_height,
                fill="lightcoral", outline="black"
            )
            self.canvas.create_text(
                x_start + box_width // 2, y_start_stack - index * box_height + box_height // 2,
                text=str(item), font=("Arial", 12, "bold")
            )
        
root = tk.Tk()
size = 4 
app = StackQueue(root, size)
root.mainloop()
