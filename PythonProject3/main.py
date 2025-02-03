import customtkinter as ctk
from database_model import DataBaseModel
from welcome_page import WelcomePage
from login_page import LoginPage
from signup_page import SignupPage
from browse_items_page import BrowseItemsPage
from cart_page import CartPage
from checkout_page import CheckoutPage
from customer_order_history import CustomerOrderHistory

class CustomerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.title("Belfast Celtic - Customer Portal")

        self.db_model = DataBaseModel("Belfast_celtic.db")
        self.cart = {}
        self.user_id = None

        self.frames = {
            "WelcomePage": WelcomePage(self),
            "LoginPage": LoginPage(self),
            "SignupPage": SignupPage(self),
            "BrowseItemsPage": BrowseItemsPage(self),
            "CartPage": CartPage(self),
            "CheckoutPage": CheckoutPage(self),
            "CustomerOrderHistory": CustomerOrderHistory(self),
        }

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_welcome_page()

    def show_welcome_page(self):
        self.frames["WelcomePage"].tkraise()

    def show_browse_items_page(self):
        self.frames["BrowseItemsPage"].update_view()
        self.frames["BrowseItemsPage"].tkraise()

    def show_customer_order_history(self):
        self.frames["CustomerOrderHistory"].update_orders()
        self.frames["CustomerOrderHistory"].tkraise()
