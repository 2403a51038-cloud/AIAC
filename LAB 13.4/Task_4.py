def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply
}

operation = input("Enter operation (add, subtract, multiply): ").strip()
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = operations.get(operation, lambda x, y: None)(a, b)
print(result)
