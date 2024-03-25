import random

class VacuumCleaner:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.current_position = (random.randint(0, rows-1), random.randint(0, cols-1))
        self.visited_cells = set()

    def move(self):
        direction = random.randint(0, 3)
        if direction == 0 and self.current_position[0] > 0:
            self.current_position = (self.current_position[0] - 1, self.current_position[1])
        elif direction == 1 and self.current_position[0] < self.rows - 1:
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
        elif direction == 2 and self.current_position[1] > 0:
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
        elif direction == 3 and self.current_position[1] < self.cols - 1:
            self.current_position = (self.current_position[0], self.current_position[1] + 1)

    def clean_room(self):
        while len(self.visited_cells) < self.rows * self.cols:
            self.visited_cells.add(self.current_position)
            self.move()
            print(f"Current position: {self.current_position}")

if __name__ == "__main__":
    rows = int(input("Enter no of rows : "))
    cols = int(input("Enter no of colomns : "))

    vacuum_cleaner = VacuumCleaner(rows, cols)
    vacuum_cleaner.clean_room()
