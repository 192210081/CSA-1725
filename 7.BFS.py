from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def BFS(self, s):
        queue, visited = [s], [s]
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            queue.extend(i for i in self.graph[s] if i not in visited)
            visited.extend(queue)
def get_user_input():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))   
    g = Graph()  
    for _ in range(edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        g.addEdge(u, v)
    start_vertex = int(input("Enter the starting vertex for BFS: "))   
    return g, start_vertex
def main():
    g, start_vertex = get_user_input()
    print("Following is Breadth First Traversal (starting from vertex {})".format(start_vertex))
    g.BFS(start_vertex)
if __name__ == "__main__":
    main()
