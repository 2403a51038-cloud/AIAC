class Graph:
    def __init__(self): self.adj = {}
    def add_edge(self, u, v):
        for a, b in [(u, v), (v, u)]: self.adj.setdefault(a, []).append(b)
    def bfs(self, s):
        vis, q, res = {s}, [s], []
        while q:
            n = q.pop(0); res.append(n)
            for nb in self.adj.get(n, []):
                if nb not in vis: vis.add(nb); q.append(nb)
        return res
    def dfs_iterative(self, s):
        vis, st, res = set(), [s], []
        while st:
            n = st.pop()
            if n not in vis:
                vis.add(n); res.append(n)
                st += [x for x in reversed(self.adj.get(n, [])) if x not in vis]
        return res
    def dfs_recursive(self, s):
        vis, res = set(), []
        def dfs(n):
            vis.add(n); res.append(n)
            for nb in self.adj.get(n, []):
                if nb not in vis: dfs(nb)
        dfs(s)
        return res
g = Graph()
for _ in range(int(input("Enter number of edges: "))):
    u, v = input().split(); g.add_edge(u, v)
s = input()
print("Adjacency List of the Graph:")
[print(f"{n}: {g.adj[n]}") for n in g.adj]
print("\nBFS Traversal:", g.bfs(s))
print("DFS Traversal (Iterative):", g.dfs_iterative(s))
print("DFS Traversal (Recursive):", g.dfs_recursive(s))
print("\nDFS Iterative and Recursive give the same result:", g.dfs_iterative(s) == g.dfs_recursive(s))
