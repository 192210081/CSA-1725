import heapq
def astar(start, goal, graph):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, start))
    while open_list:
        current_cost, current_node = heapq.heappop(open_list)
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = graph[current_node][1]
            return path[::-1]
        closed_list.add(current_node)
        for neighbor in graph[current_node][0]:
            if neighbor in closed_list:
                continue
            tentative_g_score = graph[current_node][2] + graph[current_node][0][neighbor]
            if neighbor not in [i[1] for i in open_list]:
                heapq.heappush(open_list, (tentative_g_score + heuristic(neighbor, goal), neighbor))
                graph[neighbor][1] = current_node
                graph[neighbor][2] = tentative_g_score
            else:
                for i in range(len(open_list)):
                    if open_list[i][1] == neighbor:
                        if tentative_g_score < graph[neighbor][2]:
                            heapq.heappop(open_list)
                            heapq.heappush(open_list, (tentative_g_score + heuristic(neighbor, goal), neighbor))
                            graph[neighbor][1] = current_node
                            graph[neighbor][2] = tentative_g_score
    return None
def heuristic(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
graph = {
    (0, 0): [{(0, 1): 4, (1, 0): 3}, None, 0],
    (0, 1): [{(0, 0): 4, (1, 1): 5}, None, float('inf')],
    (1, 0): [{(0, 0): 3, (1, 1): 6}, None, float('inf')],
    (1, 1): [{(0, 1): 5, (1, 0): 6}, None, float('inf')]}
start = (0, 0)
goal = (1, 1)
print(astar(start, goal, graph))
