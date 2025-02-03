import customtkinter as ctk
from tkinter import messagebox


class CheckoutPage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.label = ctk.CTkLabel(self, text="Checkout", font=("Arial", 24), text_color="green")
        self.label.pack(pady=10)

        self.address_entry = ctk.CTkEntry(self, placeholder_text="Shipping Address")
        self.address_entry.pack(pady=5)

        self.phone_entry = ctk.CTkEntry(self, placeholder_text="Phone Number")
        self.phone_entry.pack(pady=5)

        self.confirm_button = ctk.CTkButton(self, text="Confirm Order", command=self.confirm_order)
        self.confirm_button.pack(pady=10)

    def confirm_order(self):
        address = self.address_entry.get()
        phone = self.phone_entry.get()

        if not address or not phone:
            messagebox.showerror("Error", "All fields are required!")
            return

        total_price = sum(self.controller.db_model.get_product_by_id(p_id)[3] * qty
                          for p_id, qty in self.controller.cart.items())

        order_id = self.controller.db_model.create_order(self.controller.user_id, total_price, address, phone)

        for product_id, quantity in self.controller.cart.items():
            self.controller.db_model.add_order_detail(order_id, product_id, "Merchandise", quantity)

        self.controller.cart.clear()
        messagebox.showinfo("Success", "Order placed successfully!")
        self.controller.show_customer_order_history()
