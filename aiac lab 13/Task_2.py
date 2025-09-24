def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = r"C:\Users\user\OneDrive\Desktop\poem.txt"
result = read_file(file_path)
if result is not None:
    print(result)
