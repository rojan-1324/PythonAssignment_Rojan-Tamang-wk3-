from discount import final_price, TAX_RATE

products = [
    ("Laptop",      85000, 10),
    ("Headphones",  4500,  15),
    ("Phone Case",  800,   5),
    ("USB Cable",   600,   0),
]

print("Tax Rate is:", TAX_RATE)

for item in products:
    name = item[0]
    original_price = item[1]
    discount = item[2]
    total = final_price(original_price, discount)
    print(name, original_price, total)