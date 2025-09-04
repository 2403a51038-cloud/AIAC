def add(x, y):
    """
    Add two numbers together.
    
    Args:
        x (float): First number
        y (float): Second number
        
    Returns:
        float: Sum of x and y
    """
    return x + y

def subtract(x, y):
    """
    Subtract the second number from the first number.
    
    Args:
        x (float): First number (minuend)
        y (float): Second number (subtrahend)
        
    Returns:
        float: Difference of x and y (x - y)
    """
    return x - y

def multiply(x, y):
    """
    Multiply two numbers together.
    
    Args:
        x (float): First number
        y (float): Second number
        
    Returns:
        float: Product of x and y
    """
    return x * y

def divide(x, y):
    """
    Divide the first number by the second number.
    
    Args:
        x (float): First number (dividend)
        y (float): Second number (divisor)
        
    Returns:
        float or str: Quotient of x and y, or error message if division by zero
    """
    # Check for division by zero
    if y == 0:
        return "Cannot divide by zero."
    return x / y

def calculator():
    """
    Main calculator function that provides an interactive calculator interface.
    
    This function:
    - Displays a menu of available operations
    - Gets user input for operation choice and numbers
    - Performs the selected calculation
    - Displays the result
    - Handles invalid inputs gracefully
    
    Returns:
        None: Prints results and error messages
    """
    # Display calculator title and menu
    print("Simple Calculator")
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    try:
        # Get user's choice of operation
        choice = input("Enter choice (1/2/3/4): ").strip()
        
        # Get the two numbers for calculation
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Perform calculation based on user's choice
        if choice == '1':
            # Addition operation
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            # Subtraction operation
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            # Multiplication operation
            result = multiply(num1, num2)
            print(f" Result: {num1} × {num2} = {result}")
        elif choice == '4':
            # Division operation
            result = divide(num1, num2)
            print(f"Result: {num1} ÷ {num2} = {result}")
        else:
            # Handle invalid operation choice
            print(" Invalid choice. Please select 1, 2, 3, or 4.")

    except ValueError:
        # Handle error when user enters non-numeric values
        print(" Invalid input. Please enter numeric values.")

# Main program loop
while True:
    # Run the calculator function
    calculator()
    
    # Ask user if they want to continue
    cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    
    # Check if user wants to exit
    if cont != 'yes':
        print(" Exiting calculator. Have a great day!")
        break