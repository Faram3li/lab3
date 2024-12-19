def calculate_volume_surface_area(length, width, height):
    volume = length * width * height
    surface_area = 2 * (length * width + width * height + length * height)
    return volume, surface_area

length = float(input("Введіть довжину: "))
width = float(input("Введіть ширину: "))
height = float(input("Введіть висоту: "))

volume, surface_area = calculate_volume_surface_area(length, width, height)
print(f"Об'єм: {volume} куб. од.")
print(f"Площа поверхні: {surface_area} кв. од.")
