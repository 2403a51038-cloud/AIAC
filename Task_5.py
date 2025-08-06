def word_frequencies():
    text = input("Enter a string: ")
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
    for word, count in freq.items():
        print(f"{word}: {count}")

# Example usage
if __name__ == "__main__":
    word_frequencies()