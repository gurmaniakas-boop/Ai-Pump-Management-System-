import sqlite3

# Connect Database
conn = sqlite3.connect("database/petrolpump.db")

cursor = conn.cursor()

# Total Sales
cursor.execute("SELECT SUM(total_sales) FROM sales")
total_sales = cursor.fetchone()[0]

# Total Liters
cursor.execute("SELECT SUM(liters) FROM sales")
total_liters = cursor.fetchone()[0]

# Total Transactions
cursor.execute("SELECT COUNT(*) FROM sales")
transactions = cursor.fetchone()[0]

# Total Expenses
cursor.execute("SELECT SUM(amount) FROM expenses")
total_expenses = cursor.fetchone()[0]

# Handle Empty Expense
if total_expenses is None:
    total_expenses = 0

# Profit Calculation
profit = total_sales - total_expenses

print("\n===== PETROL PUMP REPORT =====")
print("Total Sales:", round(total_sales, 2))
print("Total Liters:", round(total_liters, 2))
print("Total Transactions:", transactions)
print("Total Expenses:", round(total_expenses, 2))
print("Net Profit:", round(profit, 2))

conn.close()
