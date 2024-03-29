import numpy as np

def relu(n):
    if n < 0:
        return 0
    else:
        return n

user_input = input("Enter a 3x2 matrix separated by spaces (e.g., -1 2, 2 2, 3 3): ")
user_input_rows = user_input.split(',')
inp = np.array([list(map(int, row.split())) for row in user_input_rows])

weights = [np.array([3, 3]), np.array([1, 5]), np.array([3, 3]), np.array([1, 5]), np.array([2, -1])]

for x in inp:
    node0 = relu((x * weights[0]).sum())
    node1 = relu((x * weights[1]).sum())
    node2 = relu((np.array([node0, node1]) * weights[2]).sum())
    node3 = relu((np.array([node0, node1]) * weights[3]).sum())
    op = relu((np.array([node2, node3]) * weights[4]).sum())
    print(x, op)
