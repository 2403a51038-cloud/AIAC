class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

# User-defined input for stack operations
stack = Stack()
n = int(input("Enter number of elements to push: "))
for i in range(n):
    item = input(f"Enter element {i+1}: ")
    stack.push(item)

print("Stack after pushing elements:")
while not stack.is_empty():
    print("Popped:", stack.pop())
