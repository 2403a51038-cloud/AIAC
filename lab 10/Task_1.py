def discount(p, c):
    if c == "student":
        return p * (0.9 if p > 1000 else 0.95)
    return p * 0.85 if p > 2000 else p

p = float(input("Enter the price: "))
c = input("Enter the category (student/other): ").strip().lower()
print("Discounted price:", discount(p, c))


