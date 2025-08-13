def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count

# Example usage
string = input("Enter a string: ")
vowel_count = count_vowels(string)
print(f"Number of vowels in a given string: {vowel_count}")