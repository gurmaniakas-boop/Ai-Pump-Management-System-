import sqlite3

# Connect Database
conn = sqlite3.connect("database/petrolpump.db")

# Cursor
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rupees REAL,
    liters REAL,
    price_per_liter REAL,
    total_sales REAL
)
""")

conn.commit()
conn.close()

print("Database Ready")
