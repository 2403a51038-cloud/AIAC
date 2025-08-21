
        # INSERT_YOUR_CODE
# Corrected classify_age function as per new age groups
def classify_age(age):
    if age >= 0:
        if age <= 12:
            return "Child"
        elif age <= 19:
            return "Teenager"
        elif age <= 59:
            return "Adult"
        else:
            return "Senior Citizen"
    else:
        return "Invalid Age"

# Take user input and print the classification
try:
    age_input = int(input("Enter your age: "))
    print(classify_age(age_input))
except ValueError:
    print("Please enter a valid integer for age.")
