try:
    print("Result:", float(input("Enter numerator: ")) / float(input("Enter denominator: ")))
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
