import tkinter as tk
from tkinter import messagebox

class QueueGUI:
    def __init__(self, root, size):
        self.queue = []
        self.size = size
        
        root.title("Queue Visualization")
        
        self.entry = tk.Entry(root, width=20)
        self.entry.grid(row=0, column=0, padx=10, pady=10)
        
        self.enqueue_button = tk.Button(root, text="Enqueue", command=self.enqueue, width=10)
        self.enqueue_button.grid(row=0, column=1, padx=5)
        
        self.dequeue_button = tk.Button(root, text="Dequeue", command=self.dequeue, width=10)
        self.dequeue_button.grid(row=1, column=1, padx=5)
        
        self.peek_button = tk.Button(root, text="Peek", command=self.peek, width=10)
        self.peek_button.grid(row=2, column=1, padx=5)
        
        self.canvas = tk.Canvas(root, width=400, height=100, bg="white")
        self.canvas.grid(row=1, column=0, rowspan=3, padx=10, pady=10)
        
    def enqueue(self):
        val = self.entry.get()
        if not val:
            messagebox.showwarning("Warning", "Please enter a value to enqueue")
            return
        
        if len(self.queue) == self.size:
            messagebox.showerror("Error", "Queue Overflow")
            return
        
        self.queue.append(val)
        self.update_queue_display()
        self.entry.delete(0, tk.END) 
        
    def dequeue(self):
        if len(self.queue) == 0:
            messagebox.showerror("Error", "Queue Underflow")
            return
        
        dequeued_value = self.queue.pop(0)
        self.update_queue_display()
        messagebox.showinfo("Dequeued", f"Dequeued element: {dequeued_value}")
        
    def peek(self):
        if len(self.queue) == 0:
            messagebox.showwarning("Warning", "Queue is empty")
            return
        messagebox.showinfo("Peek", f"Front element: {self.queue[0]}")
        
    def update_queue_display(self):
        self.canvas.delete("all")
        x_start = 20
        y_start = 40
        box_width = 60
        box_height = 30
        
        for index, item in enumerate(self.queue):
            self.canvas.create_rectangle(
                x_start + index * box_width, y_start, x_start + (index + 1) * box_width, y_start + box_height,
                fill="lightblue", outline="black"
            )
            self.canvas.create_text(
                x_start + index * box_width + box_width // 2, y_start + box_height // 2,
                text=str(item), font=("Arial", 12, "bold")
            )
        
root = tk.Tk()
app = QueueGUI(root, size=5) 
root.mainloop()
