import time
# Function to take user input for student records
def input_students():
    students = []
    n = int(input("Enter the number of students: "))
    for i in range(n):
        print(f"\nEnter details for student {i+1}:")
        name = input("Name: ")
        roll_no = input("Roll No: ")
        while True:
            try:
                cgpa = float(input("CGPA: "))
                break
            except ValueError:
                print("Invalid CGPA. Please enter a number.")
        students.append({'Name': name, 'Roll No': roll_no, 'CGPA': cgpa})
    return students
# Quick Sort implementation
def quick_sort_students(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]['CGPA']
    left = [x for x in arr if x['CGPA'] > pivot]
    middle = [x for x in arr if x['CGPA'] == pivot]
    right = [x for x in arr if x['CGPA'] < pivot]
    return quick_sort_students(left) + middle + quick_sort_students(right)
# Merge Sort implementation
def merge_sort_students(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_students(arr[:mid])
    right = merge_sort_students(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]['CGPA'] > right[j]['CGPA']:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# Function to get top 10 students by CGPA
def get_top_10_students(students):
    # Assume students are already sorted in descending order by CGPA
    return students[:10]
# Main execution and performance comparison
if __name__ == "__main__":
    students = input_students()
    # Quick Sort
    students_for_quick = students.copy()
    start_time = time.time()
    sorted_quick = quick_sort_students(students_for_quick)
    quick_sort_time = time.time() - start_time
    print(f"\nQuick Sort Time: {quick_sort_time:.6f} seconds")
    # Merge Sort
    students_for_merge = students.copy()
    start_time = time.time()
    sorted_merge = merge_sort_students(students_for_merge)
    merge_sort_time = time.time() - start_time
    print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")
    # Output top 10 students from one of the sorted lists
    print("\nTop 10 Students by CGPA:")
    top_10 = get_top_10_students(sorted_quick)
    for idx, student in enumerate(top_10, 1):
        print(f"{idx}. Name: {student['Name']}, Roll No: {student['Roll No']}, CGPA: {student['CGPA']}")






