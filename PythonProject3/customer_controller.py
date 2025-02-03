import customtkinter as ctk
from models.database_model import DataBaseModel
from views.welcome_page import WelcomePage
from views.login_page import LoginPage
from views.signup_page import SignupPage
from views.browse_items_page import BrowseItemsPage
from views.cart_page import CartPage
from views.checkout_page import CheckoutPage
from views.customer_details_page import CustomerDetailsPage
from views.customer_order_history import CustomerOrderHistoryPage

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
            "CustomerDetailsPage": CustomerDetailsPage(self),
            "CustomerOrderHistoryPage": CustomerOrderHistoryPage(self),
        }

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_welcome_page()

    def show_welcome_page(self):
        self.frames["WelcomePage"].tkraise()

    def show_login_page(self):
        self.frames["LoginPage"].tkraise()

    def show_signup_page(self):
        self.frames["SignupPage"].tkraise()

    def show_browse_items_page(self):
        self.frames["BrowseItemsPage"].update_view()
        self.frames["BrowseItemsPage"].tkraise()

    def show_cart_page(self):
        self.frames["CartPage"].update_cart()
        self.frames["CartPage"].tkraise()

    def show_checkout_page(self):
        self.frames["CheckoutPage"].tkraise()

    def show_customer_details_page(self):
        self.frames["CustomerDetailsPage"].update_details()
        self.frames["CustomerDetailsPage"].tkraise()

    def show_customer_order_history(self):
        self.frames["CustomerOrderHistoryPage"].update_orders()
        self.frames["CustomerOrderHistoryPage"].tkraise()
