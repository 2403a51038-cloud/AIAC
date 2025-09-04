def sum_even_odd_from_input():
    """
    Prompts the user to enter numbers and calculates the sum of even and odd numbers separately.
    This function:
    - Prompts the user to input numbers separated by spaces
    - Converts the input string to a list of integers
    - Calculates the sum of all even numbers in the input
    - Calculates the sum of all odd numbers in the input
    - Displays both sums to the user
    Input Format:
        Numbers should be entered as space-separated integers
        Example: "1 2 3 4 5 6"
    Output:
        Prints the sum of even numbers and sum of odd numbers
    Raises:
        ValueError: If the input contains non-integer values
    Example:
        >>> sum_even_odd_from_input()
        Enter numbers separated by spaces: 1 2 3 4 5 6
        Sum of even numbers: 12
        Sum of odd numbers: 9
    """
    try:
        # Get user input and prompt for numbers
        user_input = input("Enter numbers separated by spaces: ")
        
        # Convert input string to list of integers
        # strip() removes leading/trailing whitespace
        # split() splits the string by spaces into a list
        # map(int, ...) converts each string to integer
        numbers = list(map(int, user_input.strip().split()))

        # Calculate sum of even numbers using list comprehension
        # num % 2 == 0 checks if number is even (remainder is 0)
        even_sum = sum(num for num in numbers if num % 2 == 0)
        
        # Calculate sum of odd numbers using list comprehension
        # num % 2 != 0 checks if number is odd (remainder is not 0)
        odd_sum = sum(num for num in numbers if num % 2 != 0)

        # Display the results to the user
        print(f"Sum of even numbers: {even_sum}")
        print(f"Sum of odd numbers: {odd_sum}")

    except ValueError:
        # Handle error when user enters non-integer values
        print("Please enter only integers separated by spaces.")

# Call the function to execute the program
sum_even_odd_from_input()