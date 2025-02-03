import customtkinter as ctk
from database_model import DataBaseModel
from manager_order_dashboard import ManagerOrderDashboard
from manager_sales_analytics import ManagerSalesAnalytics

class ManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.title("Belfast Celtic - Manager Portal")

        self.db_model = DataBaseModel("Belfast_celtic.db")

        self.frames = {
            "ManagerOrderDashboard": ManagerOrderDashboard(self),
            "ManagerSalesAnalytics": ManagerSalesAnalytics(self),
        }

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_manager_order_dashboard()

    def show_manager_order_dashboard(self):
        self.frames["ManagerOrderDashboard"].update_orders()
        self.frames["ManagerOrderDashboard"].tkraise()

    def show_manager_sales_analytics(self):
        self.frames["ManagerSalesAnalytics"].update_sales_data()
        self.frames["ManagerSalesAnalytics"].tkraise()
