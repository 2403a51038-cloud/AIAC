full_name = input("Enter full name (First Last): ").strip()
parts = full_name.split()
if len(parts) >= 2:
    first = parts[0]
    last = " ".join(parts[1:])
    print(f"{last} , {first}")
else:
    print("Please enter both first and last names.")
