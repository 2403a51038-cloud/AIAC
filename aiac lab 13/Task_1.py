def calculate_area(shape, x, y=0):
    if shape == "rectangle":
        return x * y
    elif shape == "square":
        return x * x
    elif shape == "circle":
        return 3.14 * x * x
    else:
        return None
shape = input("Enter the shape (rectangle/square/circle): ").strip().lower()
if shape == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = calculate_area(shape, length, width)
elif shape == "square":
    side = float(input("Enter the side length: "))
    area = calculate_area(shape, side)
elif shape == "circle":
    radius = float(input("Enter the radius: "))
    area = calculate_area(shape, radius)
else:
    area = None
    print("Invalid shape entered.")
if area is not None:
    print(f"The area of the {shape} is: {area}")