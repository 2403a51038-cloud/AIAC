class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks  # marks should be a list of 3 integers
    def details(self):
        print(f"Name: {self.name} Age: {self.age}")
    def total(self):
        return sum(self.marks)
def get_student_input(): 
    name = input("Enter student's name: ").strip()
    while True:
        try:
            age = int(input("Enter student's age: "))
            break
        except ValueError:print("Invalid input for age. Please enter an integer.")
    marks = []
    for i in range(1, 4):
        while True:
            try:
                mark = int(input(f"Enter mark {i}: "))
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input for mark. Please enter an integer.")
    return Student(name, age, marks)
if __name__ == "__main__":
    student = get_student_input()
    student.details()
    total_marks = student.total()
    print("Total Marks (absolute value):", abs(total_marks))
