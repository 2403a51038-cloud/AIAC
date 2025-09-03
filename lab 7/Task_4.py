def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            if values[j] != 0:
                ratio = values[i] / values[j]
                results.append((i, j, ratio))
            else:
                results.append((i, j, None))  # Avoid division by zero
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))