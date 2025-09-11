class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

# User-defined input for queue operations
queue = Queue()
n = int(input("Enter number of elements to enqueue: "))
for i in range(n):
    item = input(f"Enter element {i+1}: ")
    queue.enqueue(item)

print("Queue after enqueuing elements:")
while not queue.is_empty():
    print("Dequeued:", queue.dequeue())

