from datetime import datetime
def find_overlapping_fields(schedules: list[dict]) -> list[tuple[str, str]]:
    intervals = []
    for entry in schedules:
        field = entry['field']
        start = datetime.fromisoformat(entry['start'])
        end = datetime.fromisoformat(entry['end'])
        intervals.append((field, start, end))
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    overlaps = set()
    for i in range(n):
        fieldA, startA, endA = intervals[i]
        for j in range(i+1, n):
            fieldB, startB, endB = intervals[j]
            if startB >= endA:break
            if startA < endB and startB < endA:pair = tuple(sorted((fieldA, fieldB)))
    overlaps.add(pair)
    return sorted(overlaps)
if __name__ == "__main__":
    import sys
    import ast
    print("Enter irrigation schedules as a Python list (each item: {'field': str, 'start': ISO, 'end': ISO})")
    user_input = ''
    while True:
        try:line = input()
        except EOFError: break
        if line.strip() == '': break
        user_input += line + '\n'
    try: schedules = ast.literal_eval(user_input)
    except Exception as e:print("Invalid input:", e)
    sys.exit(1)
    print("Input schedules:")
    for entry in schedules:print(entry)
    result = find_overlapping_fields(schedules)
    print("Overlapping field pairs:")
    print(result)



