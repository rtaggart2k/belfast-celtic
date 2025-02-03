import customtkinter as ctk
from tkinter import ttk

class ManagerOrderDashboard(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.label = ctk.CTkLabel(self, text="Manager Order Dashboard", font=("Arial", 24), text_color="green")
        self.label.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("Order ID", "Customer", "Total (£)", "Date", "Status"), show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree.heading("Order ID", text="Order ID")
        self.tree.heading("Customer", text="Customer")
        self.tree.heading("Total (£)", text="Total (£)")
        self.tree.heading("Date", text="Date Created")
        self.tree.heading("Status", text="Status")

        self.update_orders()

    def update_orders(self):
        self.tree.delete(*self.tree.get_children())
        orders = self.controller.db_model.get_all_orders()

        for order in orders:
            self.tree.insert("", "end", values=order)
