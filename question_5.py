price = float(input("Original price "))
discount = float(input("Discount in decimal form "))
new_price = "{:.2f}" . format(price * (1-discount))
print("New price is", new_price, "dollars", "after", discount *100,"% off")