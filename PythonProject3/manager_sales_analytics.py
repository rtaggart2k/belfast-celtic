import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ManagerSalesAnalytics(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.label = ctk.CTkLabel(self, text="Sales Analytics", font=("Arial", 24), text_color="green")
        self.label.pack(pady=10)

        self.chart_frame = ctk.CTkFrame(self)
        self.chart_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.update_sales_data()

    def update_sales_data(self):
        sales_data = self.controller.db_model.get_sales_data()
        labels = ['Tickets', 'Merchandise', 'Parking']
        values = [sales_data[2], sales_data[3], sales_data[4]]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        ax.set_title("Sales Breakdown")

        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
