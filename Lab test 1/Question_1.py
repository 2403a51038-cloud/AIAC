# Program to calculate the sum of odd and even numbers in a user-input list

# Get user input as a list of integers
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)