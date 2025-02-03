import customtkinter as ctk
from tkinter import messagebox

class LoginPage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.label = ctk.CTkLabel(self, text="Login", font=("Arial", 24), text_color="green")
        self.label.pack(pady=10)

        self.email_entry = ctk.CTkEntry(self, placeholder_text="Email")
        self.email_entry.pack(pady=5)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=5)

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        user = self.controller.db_model.authenticate_user(email, password)

        if user:
            self.controller.user_id = user[0]
            role = user[5]

            if role == "Customer":
                self.controller.show_browse_items_page()
            elif role == "Manager":
                self.controller.show_manager_order_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials.")
