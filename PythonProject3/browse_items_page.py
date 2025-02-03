import customtkinter as ctk
from tkinter import ttk

class BrowseItemsPage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.label = ctk.CTkLabel(self, text="Browse Items", font=("Arial", 24), text_color="green")
        self.label.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Price"), show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price (£)")

        self.add_to_cart_button = ctk.CTkButton(self, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.pack(pady=10)

        self.update_view()

    def update_view(self):
        self.tree.delete(*self.tree.get_children())
        products = self.controller.db_model.get_all_products()

        for product in products:
            self.tree.insert("", "end", values=(product[0], product[1], product[2]))

    def add_to_cart(self):
        selected_item = self.tree.focus()
        if selected_item:
            item_values = self.tree.item(selected_item, "values")
            self.controller.cart[int(item_values[0])] = self.controller.cart.get(int(item_values[0]), 0) + 1
