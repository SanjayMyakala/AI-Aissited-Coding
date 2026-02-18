# I want to create a python program for an online shopping application that includes order tracking and sales analysis features. The program should maintain customer purchase records and analyze product using classes, constructors, loops, conditional statements, and file handling.
# Each order should store order ID, customer name, product name, quantity, price per item, and order date. Whenever a new order is placed the details must be saved permanently in a file. The program should allow the operator to repeatedly perform operations such as adding a new order, viewing all order, searching an order by order ID, and Updating the quantity or price.
# Handle it for multiple orders and ensure data integrity. Take user input for order details and validate it. Implement error handling for file operations and invalid inputs.
import json
from datetime import datetime
class Order:
    def __init__(self, order_id, customer_name, product_name, quantity, price_per_item, order_date):
        self.order_id = order_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_item = price_per_item
        self.order_date = order_date

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "price_per_item": self.price_per_item,
            "order_date": self.order_date
        }
class OrderManager:
    def __init__(self, filename):
        self.filename = filename
        self.orders = self.load_orders()
    def load_orders(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    def save_orders(self):
        with open(self.filename, 'w') as file:
            json.dump(self.orders, file, indent=4)
    def add_order(self, order):
        self.orders.append(order.to_dict())
        self.save_orders()
    def view_orders(self):
        for order in self.orders:
            print(order)
    def search_order_by_id(self, order_id):
        for order in self.orders:
            if order['order_id'] == order_id:
                return order
        return None
    def update_order(self, order_id, quantity=None, price_per_item=None):
        for order in self.orders:
            if order['order_id'] == order_id:
                if quantity is not None:
                    order['quantity'] = quantity
                if price_per_item is not None:
                    order['price_per_item'] = price_per_item
                self.save_orders()
                return True
        return False
def main():
    order_manager = OrderManager('orders.json')
    while True:
        print("1. Add New Order")
        print("2. View All Orders")
        print("3. Search Order by ID")
        print("4. Update Order")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            order_id = input("Enter order ID: ")
            customer_name = input("Enter customer name: ")
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price_per_item = float(input("Enter price per item: "))
            order_date = datetime.now().strftime("%Y-%m-%d")
            order = Order(order_id, customer_name, product_name, quantity, price_per_item, order_date)
            order_manager.add_order(order)
            print("Order added successfully!")
        elif choice == '2':
            order_manager.view_orders()
        elif choice == '3':
            order_id = input("Enter order ID to search: ")
            order = order_manager.search_order_by_id(order_id)
            if order:
                print(order)
            else:
                print("Order not found.")
        elif choice == '4':
            order_id = input("Enter order ID to update: ")
            quantity = input("Enter new quantity (leave blank to keep unchanged): ")
            price_per_item = input("Enter new price per item (leave blank to keep unchanged): ")
            quantity = int(quantity) if quantity else None
            price_per_item = float(price_per_item) if price_per_item else None
            if order_manager.update_order(order_id, quantity, price_per_item):
                print("Order updated successfully!")
            else:
                print("Order not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":    
    main()