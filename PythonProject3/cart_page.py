import customtkinter as ctk
from tkinter import ttk, messagebox

class CartPage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.label = ctk.CTkLabel(self, text="Shopping Cart", font=("Arial", 24), text_color="green")
        self.label.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("Product", "Quantity", "Price (£)"), show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree.heading("Product", text="Product")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price (£)", text="Price (£)")

        self.total_label = ctk.CTkLabel(self, text="Total: £0.00", font=("Arial", 18))
        self.total_label.pack(pady=10)

        self.checkout_button = ctk.CTkButton(self, text="Proceed to Checkout", command=self.proceed_to_checkout)
        self.checkout_button.pack(pady=10)

        self.update_cart()

    def update_cart(self):
        self.tree.delete(*self.tree.get_children())
        cart = self.controller.cart
        total = 0

        for product_id, quantity in cart.items():
            product = self.controller.db_model.get_product_by_id(product_id)
            if product:
                total += product[3] * quantity
                self.tree.insert("", "end", values=(product[1], quantity, f"£{product[3] * quantity:.2f}"))

        self.total_label.configure(text=f"Total: £{total:.2f}")

    def proceed_to_checkout(self):
        self.controller.show_checkout_page()
