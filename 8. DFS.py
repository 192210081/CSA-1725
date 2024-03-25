class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()

        def dfs_helper(node):
            print(node, end=' ')
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)
        dfs_helper(start)

if __name__ == "__main__":
    g = Graph()
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        g.add_edge(u, v)

    start_node = int(input("Enter the starting node for DFS: "))

    print("DFS traversal starting from node", start_node, ":")
    g.dfs(start_node)
