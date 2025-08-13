file_path = r"C:\Users\shari\OneDrive\Desktop\lab 4.txt"

def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

print(count_lines(file_path))