def process_scores(scores):
    avg = sum(scores) / len(scores)
    print("Average:", avg)
    print("Highest:", max(scores))
    print("Lowest:", min(scores))

scores = list(map(float, input("Enter scores separated by spaces: ").split()))
process_scores(scores)
