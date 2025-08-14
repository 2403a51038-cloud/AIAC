import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_stopwords(text, stopwords):
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)

def preprocess_text():
    stopwords = {
        'a', 'an', 'the', 'and', 'or', 'but', 'if', 'while', 'with', 'to', 'of', 'at', 'by', 'for', 'from', 'in', 'on', 'off', 'out', 'over', 'under', 'as', 'is', 'it', 'this', 'that', 'these', 'those', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'so', 'such', 'no', 'not', 'too', 'very', 'can', 'will', 'just'
    }
    user_input = input("Enter your text: ")
    # Convert to lowercase
    text = user_input.lower()
    # Remove punctuation
    text = remove_punctuation(text)
    # Remove stopwords
    text = remove_stopwords(text, stopwords)
    print("Processed text:", text)

if __name__ == "__main__":
    preprocess_text()
