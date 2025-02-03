import sqlite3
from datetime import datetime

class DataBaseModel:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    # --- Customer Orders ---
    def get_orders_by_user(self, user_id):
        """Retrieve all orders placed by a specific user."""
        query = """
        SELECT id, total_price, date_created, status 
        FROM Orders 
        WHERE user_id = ? 
        ORDER BY date_created DESC
        """
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchall()

    # --- Manager Orders ---
    def get_all_orders(self):
        """Retrieve all orders in the system."""
        query = """
        SELECT Orders.id, UserAccounts.username, Orders.total_price, Orders.date_created, Orders.status 
        FROM Orders 
        JOIN UserAccounts ON Orders.user_id = UserAccounts.id 
        ORDER BY Orders.date_created DESC
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_order_status(self, order_id, status):
        """Update order status in the system."""
        query = "UPDATE Orders SET status = ? WHERE id = ?"
        self.cursor.execute(query, (status, order_id))
        self.conn.commit()

    # --- Sales Analytics ---
    def get_sales_data(self):
        """Retrieve sales breakdown for manager analytics."""
        query = """
        SELECT 
            (SELECT SUM(total_price) FROM Orders) AS total_revenue,
            (SELECT COUNT(*) FROM Orders) AS total_orders,
            (SELECT COUNT(*) FROM OrderDetails WHERE product_type = 'Ticket') AS ticket_sales,
            (SELECT COUNT(*) FROM OrderDetails WHERE product_type = 'Merchandise') AS merch_sales,
            (SELECT COUNT(*) FROM OrderDetails WHERE product_type = 'Parking') AS parking_sales
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()

    # --- Customer Details ---
    def get_customer_details(self, user_id):
        """Retrieve customer details (email, address, phone)."""
        query = """
        SELECT UserAccounts.email, CustomerDetails.address, CustomerDetails.phone 
        FROM UserAccounts 
        JOIN CustomerDetails ON UserAccounts.id = CustomerDetails.user_id 
        WHERE UserAccounts.id = ?
        """
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()
