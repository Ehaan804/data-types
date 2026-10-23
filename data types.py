snack_name = "chocalate chip cookies"
price = 10.10
quantity = 4
is_available = True

print("Snacks", snack_name)
print("Price", price)
print("Quantity", quantity)
print("In Stock", is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))

total =price * quantity
print("total value", total)
print("sale price", price - 0.10)
print("doble stock", quantity * 2)

print("is price less than 2?", price <2)
print("is quantitiy more than 5?", quantity >5)
print("is exactly 10.00", price == 10)
