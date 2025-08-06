class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"{self.name:<20} {self.roll_number:<10} {self.marks:<5}")

# Ask user for input
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
marks = input("Enter marks: ")

# Create Student object
student = Student(name, roll_number, marks)

# Display in tabular form
print("\n{:<20} {:<10} {:<5}".format("Name", "Roll No.", "Marks"))
print("-" * 37)
student.display()