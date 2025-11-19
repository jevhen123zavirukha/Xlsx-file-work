from openpyxl import Workbook
import time

wb = Workbook()
ws = wb.active

ws['A1'] = "Product"
ws['B1'] = "Price"

products_price = {"Milk": 54,
                  "Bread": 45,
                  "Water": 47,
                  "Ice": 12,
                  }

row = 2
total = 0

for product, price in products_price.items():
    ws.append([product, f"{price} $"])
    row += 1
    total += price
    time.sleep(1)

row += 1
ws[f'A{row}'] = "Total:"
ws[f'B{row}'] = f"{total} $"

wb.save("products.xlsx")
