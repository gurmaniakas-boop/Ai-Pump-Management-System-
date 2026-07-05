import sqlite3

# Connect Database
conn = sqlite3.connect("database/petrolpump.db")

cursor = conn.cursor()

# Create Expense Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    amount REAL
)
""")

conn.commit()

# Add Expense
title = input("Enter Expense Name: ")
amount = float(input("Enter Amount: "))

cursor.execute("""
INSERT INTO expenses (title, amount)
VALUES (?, ?)
""", (title, amount))

conn.commit()

print("Expense Saved Successfully")

conn.close()
