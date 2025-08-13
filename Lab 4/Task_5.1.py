file_path = r"C:\Users\shari\OneDrive\Desktop\lab 4.txt"

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(len(lines))
except FileNotFoundError:
    print(f"File not found: {file_path}")
