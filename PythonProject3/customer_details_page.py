import customtkinter as ctk

class CustomerDetailsPage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.label = ctk.CTkLabel(self, text="Your Details", font=("Arial", 24), text_color="green")
        self.label.pack(pady=10)

        self.details_text = ctk.CTkLabel(self, text="", font=("Arial", 18))
        self.details_text.pack(pady=10)

        self.update_details()

    def update_details(self):
        customer = self.controller.db_model.get_customer_details(self.controller.user_id)
        if customer:
            self.details_text.configure(text=f"Email: {customer[1]}\nAddress: {customer[2]}\nPhone: {customer[3]}")
        else:
            self.details_text.configure(text="No details available.")
