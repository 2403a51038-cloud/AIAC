def find_common(a, b):
    # Use set intersection for efficiency and uniqueness
    return list(set(a) & set(b))

# User input for two lists
a = input("Enter elements of first list separated by spaces: ").split()
b = input("Enter elements of second list separated by spaces: ").split()

result = find_common(a, b)
print("Common elements:", result)
