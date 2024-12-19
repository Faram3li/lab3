def calculate_operations(a, b):
    summa = a + b
    different = a - b
    product = a * b
    return summa, different, product

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

summa, different, product = calculate_operations(a, b)
print(f"Сума: {summa}")
print(f"Різниця: {different}")
print(f"Добуток: {product}")
