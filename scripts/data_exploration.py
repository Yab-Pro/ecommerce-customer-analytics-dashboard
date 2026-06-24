import pandas as pd

# Load datasets
customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
order_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
products = pd.read_csv("data/raw/olist_products_dataset.csv")

print("Datasets loaded successfully")

# Basic exploration
print("\nCustomers shape:", customers.shape)
print("Orders shape:", orders.shape)
print("Order Items shape:", order_items.shape)
print("Products shape:", products.shape)

print("\nCustomers preview:")
print(customers.head())