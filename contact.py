import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = {}
        
        # Create GUI elements
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        self.listbox = tk.Listbox(root)
        self.listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        # Populate listbox with existing contacts
        self.update_listbox()
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        
        if name and phone:
            self.contacts[name] = phone
            self.update_listbox()
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both name and phone number.")
            
    def delete_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_name = self.listbox.get(selected_index)
            del self.contacts[selected_name]
            self.update_listbox()
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")
            
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for name, phone in self.contacts.items():
            self.listbox.insert(tk.END, f"{name}: {phone}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
