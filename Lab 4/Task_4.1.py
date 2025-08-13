def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

input_str = input("Enter a string: ")
num_vowels = count_vowels(input_str)
print(f"Number of vowels: {num_vowels}")
