class Node:
    def __init__(self, data): self.data, self.left, self.right = data, None, None
class BST:
    def __init__(self): self.root = None
    def insert(self, data):
        def _i(n, d):
            if not n: return Node(d)
            if d < n.data: n.left = _i(n.left, d)
            elif d > n.data: n.right = _i(n.right, d)
            return n
        self.root = _i(self.root, data)
    def search(self, data):
        def _s(n, d):
            if not n: return False
            if d == n.data: return True
            return _s(n.left, d) if d < n.data else _s(n.right, d)
        return _s(self.root, data)
    def inorder_traversal(self):
        res = []
        def _in(n):
            if n: _in(n.left); res.append(n.data); _in(n.right)
        _in(self.root)
        return res
bst = BST()
for i in range(int(input("Enter number of elements to insert into BST: "))):
    bst.insert(int(input(f"Enter element {i+1}: ")))
print("BST inorder traversal (sorted):", bst.inorder_traversal())
to_search = int(input("Enter a value to search (should be present): "))
print(f"Search for {to_search}: {'Found' if bst.search(to_search) else 'Not Found'}")
to_search_absent = int(input("Enter a value to search (should be absent): "))
print(f"Search for {to_search_absent}: {'Found' if bst.search(to_search_absent) else 'Not Found'}")
