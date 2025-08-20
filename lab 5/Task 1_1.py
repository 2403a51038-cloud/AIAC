import hashlib
import uuid

# Python program to collect user data and explain anonymization


# Collect data from user
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")

print("\nOriginal Data:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Email: {email}")

# --- Anonymization using Hashing ---
# Hashing converts data into a fixed-size string that cannot be easily reversed.
# This is useful for anonymizing sensitive information like names and emails.

def hash_data(data):
    # Use SHA-256 hashing algorithm
    return hashlib.sha256(data.encode()).hexdigest()


hashed_email = hash_data(email)

print("\nAnonymized Data (using hashing):")
print(f"Name : {name}")
print(f"Age: {age}")  # Age may not need hashing unless it's sensitive
print(f"Email (hashed): {hashed_email}")

