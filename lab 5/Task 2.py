from typing import Literal

def simple_sentiment_analysis(text: str) -> Literal['positive', 'negative', 'neutral']:
    positive_words = {'good', 'great', 'excellent', 'happy', 'love', 'wonderful', 'amazing', 'fantastic', 'positive', 'joy'}
    negative_words = {'bad', 'terrible', 'awful', 'sad', 'hate', 'horrible', 'worst', 'negative', 'angry', 'disappoint'}

    text_lower = text.lower()
    pos_count = sum(word in text_lower for word in positive_words)
    neg_count = sum(word in text_lower for word in negative_words)

    if pos_count > neg_count:
        return 'positive'
    elif neg_count > pos_count:
        return 'negative'
    else:
        return 'neutral'

# Example usage:
user_input = input("Enter text for sentiment analysis: ")
result = simple_sentiment_analysis(user_input)
print(f"Sentiment: {result}")