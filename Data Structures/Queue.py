import tkinter as tk
from tkinter import messagebox

class QueueGUI:
    def __init__(self, root, size):
        self.queue = []
        self.size = size

        root.title("Queue GUI")

        self.entry = tk.Entry(root, width=20)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        self.enqueue_button = tk.Button(root, text="Enqueue", command=self.enqueue, width=10)
        self.enqueue_button.grid(row=0, column=1, padx=5)

        self.dequeue_button = tk.Button(root, text="Dequeue", command=self.dequeue, width=10)
        self.dequeue_button.grid(row=1, column=1, padx=5)

        self.peek_button = tk.Button(root, text="Peek", command=self.peek, width=10)
        self.peek_button.grid(row=2, column=1, padx=5)

        self.listbox = tk.Listbox(root, height=1, width=30)
        self.listbox.grid(row=1, column=0, rowspan=1, padx=10, pady=10)

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
        self.listbox.delete(0, tk.END)
        string_list = []
        for item in self.queue : 
            string_list.append(str(item))
        display_str = " | ".join(string_list)
        self.listbox.insert(tk.END, display_str)

root = tk.Tk()
app = QueueGUI(root, size=5) 
root.mainloop()


