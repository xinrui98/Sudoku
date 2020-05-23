# 1. pick empty square
# 2. try all numbers
# 3. find what works
# 4. repeat
# 5. backtrack
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


def solve(board):
    find = find_empty(board)
    # base case
    # if cannot find any empty spots, means we have reached the end and completed board
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        # (row,col) is empty spot, by using find
        if valid(board, i, (row, col)):
            board[row][col] = i
            # backtrack algo. after getting 1 success, go and try the next spot, if cannot solve, will return False,
            # and go back to previous recursion, set board[row][col] =0, then continue for loop to try diff values
            if solve(board):
                return True
            else:
                board[row][col] = 0
    return False


# return False to indicate that we found a duplicate
def valid(board, num, pos):
    # check row
    for i in range(len(board[0])):
        # pos[1]!=i checks if the element appears where we have just inserted it
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # check col
    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # for example element in box 1,2, to access the elements, need to *3, then it spans till *3+3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            # checks if the element appears where we have just inserted it
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(board):
    for i in range(len(board)):
        # dont want to print line on the most left
        # everytime after 3rd row, print horizontal line
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        # dont want to print line on the most left
        # everytime after 3rd col, print horizontal line
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # if last element of row, dont print horizontal line
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # row, col as tuple
                return (i, j)
    return None


print_board(board)
solve(board)
print("________solved_________")
print_board(board)
