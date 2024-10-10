#!/usr/bin/env python3
def checkmate(board):
    k_p = None
    for i, row in enumerate(board):
        if 'K' in row:
            k_p = (i, row.index('K'))
            break

    if not k_p:
        return "Fail"

    if p_atk(board, k_p) or \
       r_atk(board, k_p) or \
       b_atk(board, k_p) or \
       q_atk(board, k_p):
        print("Success")
    else:
        print("Fail")

def p_atk(board, k_p):
    row, col = k_p
    if row > 0:
        if col > 0 and board[row - 1][col - 1] == 'P':
            return True
        if col < len(board[row]) - 1 and board[row - 1][col + 1] == 'P':
            return True
    return False

def r_atk(board, k_p):
    row, col = k_p
    for i in range(col - 1, -1, -1):
        if board[row][i] == 'R':
            return True
        if board[row][i] != '.':
            break
    for i in range(col + 1, len(board[row])):
        if board[row][i] == 'R':
            return True
        if board[row][i] != '.':
            break
    for i in range(row - 1, -1, -1):
        if board[i][col] == 'R':
            return True
        if board[i][col] != '.':
            break
    for i in range(row + 1, len(board)):
        if board[i][col] == 'R':
            return True
        if board[i][col] != '.':
            break
    for i in range(row + 1, len(board)):
        if board[i][col] == 'R':
            return True
        if board[i][col] != '.':
            break
    for i in range(row + 1, len(board)):
        if board[i][col] == 'R':
            return True
        if board[i][col] != '.':
            break
    for i in range(row + 1, len(board)):
        if board[i][col] == 'R':
            return True
        if board[i][col] != '.':
            break
    for i in range(row + 1, len(board)):
        if board[i][col] == 'R':
            return True
        if board[i][col] != '.':
            break

    return False

def b_atk(board, k_p):
    row, col = k_p
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'B':
            return True
        if board[i][j] != '.':
            break
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board[row]):
        if board[i][j] == 'B':
            return True
        if board[i][j] != '.':
            break
        i -= 1
        j += 1

    i, j = row + 1, col - 1
    while i < len(board) and j >= 0:
        if board[i][j] == 'B':
            return True
        if board[i][j] != '.':
            break
        i += 1
        j -= 1

    i, j = row + 1, col + 1
    while i < len(board) and j < len(board[row]):
        if board[i][j] == 'B':
            return True
        if board[i][j] != '.':
            break
        i += 1
        j += 1
    while i < len(board) and j < len(board[row]):
        if board[i][j] == 'B':
            return True
        if board[i][j] != '.':
            break
        i += 1
        j += 1
    while i < len(board) and j < len(board[row]):
        if board[i][j] == 'B':
            return True
        if board[i][j] != '.':
            break
        i += 1
        j += 1
    while i < len(board) and j < len(board[row]):
        if board[i][j] == 'B':
            return True
        if board[i][j] != '.':
            break
        i += 1
        j += 1
    while i < len(board) and j < len(board[row]):
        if board[i][j] == 'B':
            return True
        if board[i][j] != '.':
            break
        i += 1
        j += 1

def q_atk(board, k_p):return r_atk(board, k_p) or b_atk(board, k_p)
def main():
    board = [
        "........",
        "........",
        "........",
        "...Q....",
        "...K....",
        "........",
        "........",
        "........",
]
    checkmate(board)

if __name__ == "__main__":
    main()
