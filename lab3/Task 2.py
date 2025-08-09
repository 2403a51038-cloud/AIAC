def sort_numbers():
    try:
        numbers = input("Enter numbers separated by spaces: ")
        num_list = [int(num) for num in numbers.strip().split()]
        sorted_list = sorted(num_list)
        print("Sorted numbers:", ' '.join(str(num) for num in sorted_list))
    except ValueError:
        print("Please enter valid integers only.")

if __name__ == "__main__":
    sort_numbers()
