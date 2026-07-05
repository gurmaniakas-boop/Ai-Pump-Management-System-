import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import easyocr
import re

# Load OCR
reader = easyocr.Reader(['en'])

# Read Image
result = reader.readtext('images/meter.jpg')

# Extract Text
texts = [item[1] for item in result]

# Extract Numbers
numbers = []

for text in texts:
    found = re.findall(r'\d+', text)

    for num in found:
        numbers.append(num)

print("Detected Numbers:")
print(numbers)

# Example Extraction
# numbers[0] = total rupees
# numbers[1] = liters
# numbers[2] = price per liter

if len(numbers) >= 3:

    rupees = float(numbers[0])
    liters = float(numbers[1]) / 100
    price_per_liter = float(numbers[2]) / 100

    total_sales = liters * price_per_liter

    print("\n--- SALES REPORT ---")
    print("Rupees:", rupees)
    print("Liters Sold:", liters)
    print("Price Per Liter:", price_per_liter)
    print("Calculated Sales:", round(total_sales, 2))

else:
    print("Not enough numbers detected.")
