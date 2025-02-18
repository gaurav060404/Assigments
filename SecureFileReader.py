import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class SecureFileReader:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure File Reader")
        self.root.geometry("500x400")

        self.open_button = tk.Button(root, text="Open File", command=self.open_file, padx=10, pady=5)
        self.open_button.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
        self.text_area.pack(pady=5)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if not file_path:
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END) 
                self.text_area.insert(tk.END, content)  

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found! Please select a valid file.")
        except PermissionError:
            messagebox.showerror("Error", "Permission denied! You don't have access to this file.")
        except UnicodeDecodeError:
            messagebox.showerror("Error", "Unable to read file! Unsupported text format.")
        except Exception as e:
            messagebox.showerror("Unexpected Error", f"An unexpected error occurred:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    SecureFileReader(root)
    root.mainloop()
