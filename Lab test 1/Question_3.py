def convert_temperature():
    print("Temperature Converter")
    print("Enter temperature (e.g., 20 C, 30 F, 300 K):")
    user_input = input().strip()
    try:
        value, unit = user_input.split()
        value = float(value)
        unit = unit.upper()
        if unit == 'C':
            f = value * 9/5 + 32
            k = value + 273.15
            print(f"{value} C = {f:.2f} F, {k:.2f} K")
        elif unit == 'F':
            c = (value - 32) * 5/9
            k = c + 273.15
            print(f"{value} F = {c:.2f} C, {k:.2f} K")
        elif unit == 'K':
            c = value - 273.15
            f = c * 9/5 + 32
            print(f"{value} K = {c:.2f} C, {f:.2f} F")
        else:
            print("Invalid unit. Use C, F, or K.")
    except Exception:
        print("Invalid input format. Example: 20 C")

if __name__ == "__main__":
    convert_temperature()