price = float(input("Введите сумму заказа:"))
tip = price * 0.18
tax = price * 0.04
print("Налог:", tax)
print("Чаевые:", tip)
print("Итог:", price + tax + tip)
