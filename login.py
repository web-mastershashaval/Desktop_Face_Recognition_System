import tkinter as tk
from tkinter import messagebox
import os
from main import Face_Recognition_System

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")

        # Username and password fields
        tk.Label(root, text="Username").pack(pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Password").pack(pady=10)
        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.pack(pady=5)

        # Login button
        tk.Button(root, text="Login", command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Hardcoded credentials (for demonstration purposes)
        if username == "admin" and password == "password":
            self.root.destroy()
            self.open_main_window()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_main_window(self):
        main_root = tk.Tk()
        app = Face_Recognition_System(main_root)
        main_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
