def calculate_bill(present_units, previous_units, purpose):
    if present_units < previous_units:
        raise ValueError("Present units cannot be less than previous units.")
    units_consumed = present_units - previous_units
    if purpose.lower() == "domestic":
        rate = 5.0  # per unit rate for domestic
    elif purpose.lower() == "industrial":
        rate = 8.0  # per unit rate for industrial
    else:
        raise ValueError("Invalid purpose. Please enter 'Domestic' or 'Industrial'.")
    amount = units_consumed * rate
    return units_consumed, rate, amount

def print_step_by_step(house_number, present_units, previous_units, purpose, units_consumed, rate, amount):
    print("\n--- Electricity Bill Calculation ---")
    print(f"House Number: {house_number}")
    print(f"Purpose: {purpose.capitalize()}")
    print(f"Previous Units: {previous_units}")
    print(f"Present Units: {present_units}")
    print(f"Step 1: Units Consumed = Present Units - Previous Units = {present_units} - {previous_units} = {units_consumed}")
    print(f"Step 2: Rate per Unit for {purpose.capitalize()} purpose = Rs. {rate:.2f}")
    print(f"Step 3: Total Amount = Units Consumed x Rate = {units_consumed} x {rate:.2f} = Rs. {amount:.2f}")
    print(f"\nTotal Electricity Bill: Rs. {amount:.2f}")

if __name__ == "__main__":
    print("Electricity Bill Calculator")
    print("---------------------------")
    try:
        house_number = input("Enter House Number: ").strip()
        previous_units = int(input("Enter Previous Units: ").strip())
        present_units = int(input("Enter Present Units: ").strip())
        purpose = input("Enter Purpose (Domestic/Industrial): ").strip()
        units_consumed, rate, amount = calculate_bill(present_units, previous_units, purpose)
        print_step_by_step(house_number, present_units, previous_units, purpose, units_consumed, rate, amount)
    except ValueError as e:
        print("Error:", e)
