import tkinter as tk
from tkinter import messagebox
import csv

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes and Password Manager")

        self.note_label = tk.Label(root, text="Notes")
        self.note_label.pack()

        self.note_title_entry = tk.Entry(root)
        self.note_title_entry.pack()

        self.note_content_text = tk.Text(root, height=10, width=40)
        self.note_content_text.pack()

        self.add_note_button = tk.Button(root, text="Add Note", command=self.add_note)
        self.add_note_button.pack()

        self.view_notes_button = tk.Button(root, text="View Notes", command=self.view_notes)
        self.view_notes_button.pack()

        self.pass_label = tk.Label(root, text="Passwords")
        self.pass_label.pack()

        self.website_entry = tk.Entry(root)
        self.website_entry.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()
        self.password_entry = tk.Entry(root)
        self.password_entry.pack()

        self.add_password_button = tk.Button(root, text="Add Password", command=self.add_password)
        self.add_password_button.pack()

        self.view_passwords_button = tk.Button(root, text="View Passwords", command=self.view_passwords)
        self.view_passwords_button.pack()

    def add_note(self):
        title = self.note_title_entry.get()
        content = self.note_content_text.get(1.0, tk.END)

        if not title or not content.strip():
            messagebox.showerror("Error", "Both title and content are required.")
            return

        with open('notes.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, content])

        self.note_title_entry.delete(0, tk.END)
        self.note_content_text.delete(1.0, tk.END)
        messagebox.showinfo("Info", "Note added successfully!")

    def view_notes(self):
        self.notes_window = tk.Toplevel(self.root)
        self.notes_window.title("Notes")

        with open('notes.csv', 'r') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                note = f"Title: {row[0]}\nContent: {row[1]}"
                label = tk.Label(self.notes_window, text=note, borderwidth=1, relief="solid", padx=10, pady=10)
                label.pack(pady=10)

    def add_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not website or not username or not password:
            messagebox.showerror("Error", "All fields are required.")
            return

        with open('passwords.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([website, username, password])

        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        messagebox.showinfo("Info", "Password added successfully!")

    def view_passwords(self):
        self.passwords_window = tk.Toplevel(self.root)
        self.passwords_window.title("Passwords")

        with open('passwords.csv', 'r') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                entry = f"Website: {row[0]}, Username: {row[1]}, Password: {row[2]}"
                label = tk.Label(self.passwords_window, text=entry, borderwidth=1, relief="solid", padx=10, pady=10)
                label.pack(pady=10)

root = tk.Tk()
app = App(root)
root.mainloop()











