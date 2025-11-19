
def merge_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    print(f"Merged {left_arr} and {right_arr} -> {arr[left:right + 1]}")

def main():
    try:
        user_input = input("Enter integers separated by spaces or commas: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nNo input provided. Exiting.")
        return

    if not user_input:
        print("No numbers entered. Exiting.")
        return

    # allow commas or mixed separators
    tokens = user_input.replace(",", " ").split()
    try:
        numbers = list(map(int, tokens))
    except ValueError:
        print("Invalid input: please enter only integers.")
        return

    print(f"\nOriginal list: {numbers}")
    if len(numbers) > 1:
        print("\nMerge steps:")
        merge_sort(numbers)
    print(f"\nSorted list: {numbers}")

if __name__ == "__main__":
    main()