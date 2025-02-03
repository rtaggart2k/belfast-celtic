import customtkinter as ctk
from tkinter import messagebox

class SignupPage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.label = ctk.CTkLabel(self, text="Sign Up", font=("Arial", 24), text_color="green")
        self.label.pack(pady=10)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username")
        self.username_entry.pack(pady=5)

        self.surname_entry = ctk.CTkEntry(self, placeholder_text="Surname")
        self.surname_entry.pack(pady=5)

        self.email_entry = ctk.CTkEntry(self, placeholder_text="Email")
        self.email_entry.pack(pady=5)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=5)

        self.signup_button = ctk.CTkButton(self, text="Sign Up", command=self.signup)
        self.signup_button.pack(pady=10)

    def signup(self):
        username = self.username_entry.get()
        surname = self.surname_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not (username and surname and email and password):
            messagebox.showerror("Error", "All fields are required.")
            return

        self.controller.db_model.add_user(username, surname, email, password, "Customer")
        messagebox.showinfo("Success", "Account created!")
        self.controller.show_login_page()
