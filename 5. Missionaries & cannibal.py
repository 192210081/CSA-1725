from queue import Queue

class State:
    def __init__(self, left_m, left_c, boat, right_m, right_c):
        self.left_m = left_m
        self.left_c = left_c
        self.boat = boat
        self.right_m = right_m
        self.right_c = right_c

    def is_valid(self):
        if (
            0 <= self.left_m <= 3 and
            0 <= self.left_c <= 3 and
            0 <= self.right_m <= 3 and
            0 <= self.right_c <= 3 and
            (self.left_m == 0 or self.left_m >= self.left_c) and
            (self.right_m == 0 or self.right_m >= self.right_c)
        ):
            return True
        return False

    def is_goal(self):
        return self.left_m == 0 and self.left_c == 0

    def _eq_(self, other):
        return (
            self.left_m == other.left_m and
            self.left_c == other.left_c and
            self.boat == other.boat and
            self.right_m == other.right_m and
            self.right_c == other.right_c
        )
    def _hash_(self):
        return hash((self.left_m, self.left_c, self.boat, self.right_m, self.right_c))

def get_successors(state):
    successors = []
    if state.boat == 'left':
        successors.append(State(state.left_m - 1, state.left_c, 'right', state.right_m + 1, state.right_c))
        successors.append(State(state.left_m - 2, state.left_c, 'right', state.right_m + 2, state.right_c))
        successors.append(State(state.left_m, state.left_c - 1, 'right', state.right_m, state.right_c + 1))
        successors.append(State(state.left_m, state.left_c - 2, 'right', state.right_m, state.right_c + 2))
        successors.append(State(state.left_m - 1, state.left_c - 1, 'right', state.right_m + 1, state.right_c + 1))
    else:
        successors.append(State(state.left_m + 1, state.left_c, 'left', state.right_m - 1, state.right_c))
        successors.append(State(state.left_m + 2, state.left_c, 'left', state.right_m - 2, state.right_c))
        successors.append(State(state.left_m, state.left_c + 1, 'left', state.right_m, state.right_c - 1))
        successors.append(State(state.left_m, state.left_c + 2, 'left', state.right_m, state.right_c - 2))
        successors.append(State(state.left_m + 1, state.left_c + 1, 'left', state.right_m - 1, state.right_c - 1))
    return [succ for succ in successors if succ.is_valid()]

def breadth_first_search():
    start_state = State(3, 3, 'left', 0, 0)
    if start_state.is_goal():
        return [start_state]

    visited = set()
    queue = Queue()
    queue.put([start_state])

    while not queue.empty():
        path = queue.get()
        current_state = path[-1]
        for successor in get_successors(current_state):
            if successor not in visited:
                new_path = list(path)
                new_path.append(successor)
                visited.add(successor)

                if successor.is_goal():
                    return new_path

                queue.put(new_path)

    return None
def print_solution(solution):
    for i, state in enumerate(solution):
        print(f"Step {i + 1}: {state.left_m}M {state.left_c}C {state.boat} | {state.right_m}M {state.right_c}C")

if __name__ == "__main__":
    solution = breadth_first_search()

    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found.")
