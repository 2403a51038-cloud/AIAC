# Program to format full names as "Last, First"

# Get full name from user
full_name = input("Enter your full name: ").strip()

# Split the name into parts
name_parts = full_name.split()

# Check if there are at least two parts
if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = name_parts[-1]
    formatted_name = f"{last_name} , {first_name}"
    print("Formatted name:", formatted_name)
else:
    print("Please enter both first and last names.")