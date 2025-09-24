nums = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in nums.strip().split()]
squares = [i * i for i in nums]
print("Squares:", squares)
