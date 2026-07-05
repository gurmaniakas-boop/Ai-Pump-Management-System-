import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import easyocr
import re

# Load OCR
reader = easyocr.Reader(['en'])

# Read Image
result = reader.readtext('images/meter.jpg')

# Extract Only Text
texts = [item[1] for item in result]

print("Detected Text:")
print(texts)

# Extract Numbers Only
numbers = []

for text in texts:
    found = re.findall(r'\d+', text)
    
    for num in found:
        numbers.append(num)

print("\nDetected Numbers:")

if len(numbers) >= 3:

    rupees = float(numbers[0])
    liters = float(numbers[1]) / 100
    price_per_liter = float(numbers[2]) / 100

    calculated_sales = liters * price_per_liter

    print("\n--- SALES REPORT ---")
    print("Rupees:", rupees)
    print("Liters Sold:", liters)
    print("Price Per Liter:", price_per_liter)
    print("Calculated Sales:", round(calculated_sales, 2))

else:
    print("Not enough numbers detected in image")
    

print("\n--- SALES REPORT ---")
print("Rupees:", rupees)
print("Liters Sold:", liters)
print("Price Per Liter:", price_per_liter)
print("Calculated Sales:", round(calculated_sales, 2))
print(numbers)
import sqlite3

# Connect Database
conn = sqlite3.connect("database/petrolpump.db")
cursor = conn.cursor()

# Insert Data
cursor.execute("""
INSERT INTO sales (rupees, liters, price_per_liter, total_sales)
VALUES (?, ?, ?, ?)
""", (rupees, liters, price_per_liter, calculated_sales))

conn.commit()
conn.close()

print("Data Saved Successfully")
