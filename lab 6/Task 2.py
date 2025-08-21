def print_multiples(n):
    print(f"First 10 multiples of {n} using FOR loop:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

    print(f"\nFirst 10 multiples of {n} using WHILE loop:")
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n * i}")
        i += 1


n = int(input("Enter a number to print its first 10 multiples: "))
print_multiples(n)