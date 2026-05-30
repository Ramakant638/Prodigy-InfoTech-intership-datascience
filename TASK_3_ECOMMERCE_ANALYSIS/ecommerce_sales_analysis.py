# TASK 3: E-COMMERCE ANALYSIS
# E-Commerce Sales Analysis using Python
# Data Science Internship Project

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create e-commerce sales database manually
ecommerce_data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    "Customer_Name": [
        "Amit", "Riya", "Rahul", "Sneha", "Karan",
        "Priya", "Vikas", "Neha", "Arjun", "Simran"
    ],
    "Product": [
        "Mobile", "Laptop", "Headphones", "Shoes", "Watch",
        "Mobile", "Bag", "Laptop", "Shoes", "Headphones"
    ],
    "Category": [
        "Electronics", "Electronics", "Electronics", "Fashion", "Accessories",
        "Electronics", "Fashion", "Electronics", "Fashion", "Electronics"
    ],
    "Quantity": [1, 1, 2, 1, 1, 2, 1, 1, 3, 1],
    "Price": [15000, 55000, 2000, 3000, 2500, 15000, 1800, 55000, 3000, 2000],
    "Payment_Mode": [
        "UPI", "Credit Card", "Cash on Delivery", "UPI", "Debit Card",
        "UPI", "Cash on Delivery", "Credit Card", "UPI", "Debit Card"
    ]
}

# Step 2: Convert database into DataFrame
data = pd.DataFrame(ecommerce_data)

# Step 3: Calculate total amount for each order
data["Total_Amount"] = data["Quantity"] * data["Price"]

# Step 4: Display database
print("E-Commerce Sales Database:")
print(data)

# Step 5: Calculate total sales
total_sales = data["Total_Amount"].sum()
print("\nTotal Sales Amount:", total_sales)

# Step 6: Product-wise sales analysis
product_sales = data.groupby("Product")["Total_Amount"].sum()
print("\nProduct-wise Sales:")
print(product_sales)

# Step 7: Category-wise sales analysis
category_sales = data.groupby("Category")["Total_Amount"].sum()
print("\nCategory-wise Sales:")
print(category_sales)

# Step 8: Payment mode analysis
payment_count = data["Payment_Mode"].value_counts()
print("\nPayment Mode Count:")
print(payment_count)

# Step 9: Best-selling product by quantity
best_product = data.groupby("Product")["Quantity"].sum().idxmax()
best_quantity = data.groupby("Product")["Quantity"].sum().max()

print("\nBest Selling Product:", best_product)
print("Total Quantity Sold:", best_quantity)

# Step 10: Highest order amount
highest_order = data.loc[data["Total_Amount"].idxmax()]
print("\nHighest Order Details:")
print(highest_order)

# Step 11: Category-wise sales graph
plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Category-wise Sales Analysis")
plt.xlabel("Category")
plt.ylabel("Total Sales Amount")
plt.grid(True)
plt.show()

# Step 12: Product-wise sales graph
plt.figure(figsize=(10, 5))
product_sales.plot(kind="bar")
plt.title("Product-wise Sales Analysis")
plt.xlabel("Product")
plt.ylabel("Total Sales Amount")
plt.grid(True)
plt.show()

# Step 13: Payment mode graph
plt.figure(figsize=(8, 5))
payment_count.plot(kind="bar")
plt.title("Payment Mode Analysis")
plt.xlabel("Payment Mode")
plt.ylabel("Number of Orders")
plt.grid(True)
plt.show()

# Step 14: Quantity sold graph
quantity_sales = data.groupby("Product")["Quantity"].sum()

plt.figure(figsize=(10, 5))
quantity_sales.plot(kind="bar")
plt.title("Product Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.grid(True)
plt.show()

print("\nConclusion:")
print("This project analyzes e-commerce sales data using Python, Pandas, and Matplotlib.")
print("It finds total sales, product-wise sales, category-wise sales, best-selling product, and payment mode analysis.")
