board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
] 

def print_board(_board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(_board[i][j])
            else:
                print(str(_board[i][j]), end=" ")




def valid(_board, num, pos):
    
    for i in range(9):
        if _board[pos[0]][i] == num and pos[1] != i:
            return False

    
    for i in range(9):
        if _board[i][pos[1]] == num and pos[0] != i:
            return False

    
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if _board[i][j] == num and (i,j) != pos:
                return False

    return True




def find_empty(_board):
    for i in range(9):
        for j in range(9):
            if _board[i][j] == 0:
                return (i, j) 

    return None

def solve(_board):
    find = find_empty(_board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(_board, i, (row, col)):
            _board[row][col] = i

            if solve(_board):
                return True

            _board[row][col] = 0

    return False

    
print_board(board)
solve(board)
print("\n__________solvd!__________\n")
print_board(board)