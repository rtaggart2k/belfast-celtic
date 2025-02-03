import customtkinter as ctk
from tkinter import ttk

class CustomerOrderHistoryPage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        # Page Title
        self.label = ctk.CTkLabel(self, text="Your Order History", font=("Arial", 24), text_color="green")
        self.label.pack(pady=10)

        # Orders Table
        self.tree = ttk.Treeview(self, columns=("Order ID", "Total (£)", "Date", "Status"), show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree.heading("Order ID", text="Order ID")
        self.tree.heading("Total (£)", text="Total (£)")
        self.tree.heading("Date", text="Date Created")
        self.tree.heading("Status", text="Status")

        self.refresh_button = ctk.CTkButton(self, text="Refresh Orders", command=self.update_orders)
        self.refresh_button.pack(pady=10)

        self.update_orders()

    def update_orders(self):
        """Fetch and display the customer's past orders."""
        self.tree.delete(*self.tree.get_children())  # Clear previous entries
        user_id = self.controller.user_id
        orders = self.controller.db_model.get_orders_by_user(user_id)

        for order in orders:
            self.tree.insert("", "end", values=order)
