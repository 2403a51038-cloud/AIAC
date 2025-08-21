def sum_to_n_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

def sum_to_n_formula(n):
    return n * (n + 1) // 2  

n = int(input("Enter a number: "))
print("Sum of first", n, "numbers (for loop):", sum_to_n_for(n))
print("Sum of first", n, "numbers (while loop):", sum_to_n_while(n))
print("Sum of first", n, "numbers (formula):", sum_to_n_formula(n))
