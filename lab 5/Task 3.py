import random

# Sample product database with brands and categories
products = [
    {"name": "BrandA Shampoo", "brand": "BrandA", "category": "Shampoo"},
    {"name": "BrandB Shampoo", "brand": "BrandB", "category": "Shampoo"},
    {"name": "BrandC Conditioner", "brand": "BrandC", "category": "Conditioner"},
    {"name": "BrandA Conditioner", "brand": "BrandA", "category": "Conditioner"},
    {"name": "BrandB Hair Oil", "brand": "BrandB", "category": "Hair Oil"},
    {"name": "BrandC Hair Oil", "brand": "BrandC", "category": "Hair Oil"},
]

# User purchase history and feedback
user_history = []
user_feedback = {}

def recommend_products(history, feedback):
    # Find categories the user bought before
    categories = set([p['category'] for p in history])
    # Brands the user liked less
    disliked_brands = {prod['brand'] for prod, fb in feedback.items() if fb == 'dislike'}
    # Brands the user liked
    liked_brands = {prod['brand'] for prod, fb in feedback.items() if fb == 'like'}

    recommendations = []
    for cat in categories:
        # Filter products in the same category, avoid disliked brands, and vary brands
        candidates = [p for p in products if p['category'] == cat and p['brand'] not in disliked_brands]
        # Prefer brands not already bought, or liked brands
        candidates = sorted(candidates, key=lambda p: (p['brand'] in liked_brands, random.random()), reverse=True)
        if candidates:
            prod = candidates[0]
            # Explain why suggested
            explanation = f"Suggested '{prod['name']}' because you bought {cat} before, and it's a different brand for fairness."
            recommendations.append((prod, explanation))
    return recommendations

def get_feedback(product):
    # Ask user for feedback
    while True:
        fb = input(f"Do you like '{product['name']}'? (like/dislike): ").strip().lower()
        if fb in ['like', 'dislike']:
            return fb
        print("Please enter 'like' or 'dislike'.")

def main():
    print("Welcome to the Product Recommender!")
    # Simulate user purchase history
    while True:
        print("\nAvailable products:")
        for idx, prod in enumerate(products):
            print(f"{idx+1}. {prod['name']} ({prod['brand']}, {prod['category']})")
        choice = input("Enter the number of a product you bought (or 'done' to finish): ").strip()
        if choice.lower() == 'done':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(products):
            user_history.append(products[int(choice)-1])
        else:
            print("Invalid choice. Try again.")

    # Recommend products
    recommendations = recommend_products(user_history, user_feedback)
    for prod, explanation in recommendations:
        print(f"\nRecommendation: {prod['name']}")
        print("Reason:", explanation)
        fb = get_feedback(prod)
        user_feedback[tuple(prod.items())] = fb  # Store feedback

    print("\nThank you for your feedback! Recommendations will improve over time.")

if __name__ == "__main__":
    main()