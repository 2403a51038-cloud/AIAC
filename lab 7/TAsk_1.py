def factr_correct(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factr_correct(n - 1)

print(factr_correct(5))