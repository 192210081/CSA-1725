def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        return True

def solve_n_queens_util(board, col):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1  
         
            if solve_n_queens_util(board, col + 1):
                return True
            
            board[i][col] = 0

    
    return False


def solve_n_queens():
    board = [[0] * N for _ in range(N)]

    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False

    print_board(board)
    return True


def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


if __name__ == "__main__":
    N = 8  
    solve_n_queens()
