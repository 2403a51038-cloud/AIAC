class SRU_Student:
    """
    A class to represent a student at SRU (Shri Ramswaroop Memorial University).
    
    This class manages student information including name, roll number, hostel status,
    and fee payments. It provides methods to update fees and display student details.
    
    Attributes:
        name (str): The student's full name
        roll_no (str): The student's roll number
        hostel_status (str): Whether the student is staying in hostel (Yes/No)
        fee (float): Total fee amount paid by the student
    
    Methods:
        fee_update(amount): Updates the student's fee payment
        display_details(): Displays all student information
    """
    
    def __init__(self, name, roll_no, hostel_status):
        """
        Initialize a new SRU_Student object.
        
        Args:
            name (str): The student's full name
            roll_no (str): The student's roll number
            hostel_status (str): Hostel status (Yes/No)
        """
        # Initialize student attributes
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        # Initialize fee to 0 for new students
        self.fee = 0
    
    def fee_update(self, amount):
        """
        Update the student's fee payment.
        
        This method adds the specified amount to the student's total fee.
        It validates that the amount is not negative before updating.
        
        Args:
            amount (float): The fee amount to add (must be non-negative)
            
        Returns:
            None: Prints confirmation message or error message
        """
        # Check if the fee amount is negative
        if amount < 0:
            print(" Fee amount cannot be negative.")
        else:
            # Add the amount to current fee total
            self.fee += amount
            # Display updated fee information
            print(f"Fee updated. Current total fee: ₹{self.fee}")
    
    def display_details(self):
        """
        Display all student information in a formatted manner.
        
        This method prints the student's name, roll number, hostel status,
        and total fee paid in a well-formatted table.
        
        Returns:
            None: Prints formatted student details
        """
        # Print header for student details
        print("\n ----- Student Details -----")
        # Display student name
        print(f"Name           : {self.name}")
        # Display roll number
        print(f"Roll No.       : {self.roll_no}")
        # Display hostel status
        print(f"Hostel Status  : {self.hostel_status}")
        # Display total fee paid
        print(f"Total Fee Paid : ₹{self.fee}")
        # Print footer
        print("-----------------------------\n")

# Get student information from user input
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
hostel_status = input("Hostel status (Yes/No): ")

# Create a new student object with the provided information
student = SRU_Student(name, roll_no, hostel_status)

try:
    # Get fee amount from user and convert to float
    fee_amount = float(input("Enter fee amount to update: ₹"))
    # Update the student's fee
    student.fee_update(fee_amount)
except ValueError:
    # Handle error when user enters non-numeric fee amount
    print("Invalid input. Please enter a numeric fee amount.")

# Display the complete student details
student.display_details()