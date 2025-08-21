# Step 1: Define the Student class
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display_details(self):
        print("--------Student Details-------")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")
    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'Fail'
# Step 2: Take user input for number of students
num_students = int(input("Enter number of students: "))
students = []
# Step 3: Take details for each student and create Student objects
for i in range(num_students):
    print(f"\nEnter details for student {i+1}:")
    name = input("Enter student name: ")
    roll_no = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))
    student = Student(name, roll_no, marks)
    students.append(student)
# Step 4: Display all student details
print("\nAll Student Details:")
for student in students:
    student.display_details()