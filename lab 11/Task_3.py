class Node:
    def __init__(self, data): self.data, self.next = data, None
class LinkedList:
    def __init__(self): self.head = None
    def insert_at_end(self, data):
        if not self.head: self.head = Node(data); return
        cur = self.head
        while cur.next: cur = cur.next
        cur.next = Node(data)
    def delete_value(self, value):
        cur, prev = self.head, None
        while cur:
            if cur.data == value:
                if prev: prev.next = cur.next
                else: self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False
    def traverse(self):
        res, cur = [], self.head
        while cur: res.append(cur.data); cur = cur.next
        return res
ll = LinkedList()
for i in range(int(input("Enter number of elements to insert at end: "))):
    ll.insert_at_end(input(f"Enter element {i+1}: "))
print("Linked List after insertions:\n", ll.traverse())
for i in range(int(input("Enter number of elements to delete by value: "))):
    val = input(f"Enter value to delete ({i+1}): ")
    print(f"{'Deleted' if ll.delete_value(val) else 'Value '+val+' not found in'} the list.")
    print("Current Linked List:", ll.traverse())
