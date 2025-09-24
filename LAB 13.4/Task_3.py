student_scores = {"Alice": 85, "Bob": 90}
name = input("Enter student name: ")
result = student_scores.get(name, "Not Found")
print(result)
