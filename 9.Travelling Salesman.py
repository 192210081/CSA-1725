from sys import maxsize
from itertools import permutations

def travellingSalesmanProblem(graph, s):
    vertex = [i for i in range(len(graph)) if i != s]
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
    return min_path

if __name__ == "__main__":
    num_cities = int(input("Enter the number of cities: "))
    graph = []
    print("Enter the distance matrix ({}x{}):".format(num_cities, num_cities))
    for _ in range(num_cities):
        row = list(map(int, input().split()))
        graph.append(row)

    start_city = int(input("Enter the starting city index: "))
    print(travellingSalesmanProblem(graph, start_city))
