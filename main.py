#!/usr/bin/env python3

def checkmate(board):
    k_p = None
    for i, row in enumerate(board):
        if 'K' in row:
            k_p = (i, row.index('K'))
            break

    if k_p is None:
        print("King not found on the board")
        return

    if p_atk(board, k_p) or r_atk(board, k_p) or b_atk(board, k_p) or q_atk(board, k_p):
        print("Success")
    else:
        print("Fail")

def p_atk(board, k_p):
    row, col = k_p
    return ((row < len(board) - 1 and col > 0 and board[row + 1][col - 1] == 'P') or
            (row < len(board) - 1 and col < len(board[row]) - 1 and board[row + 1][col + 1] == 'P'))

def r_atk(board, k_p):
    row, col = k_p
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
    for d_row, d_col in directions:
        i, j = row, col
        while 0 <= i + d_row < len(board) and 0 <= j + d_col < len(board[i]):
            i += d_row
            j += d_col
            if board[i][j] == 'R' or board[i][j] == 'Q':
                return True
            if board[i][j] != '.':
                break
    return False

def b_atk(board, k_p):
    row, col = k_p
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  
    for d_row, d_col in directions:
        i, j = row, col
        while 0 <= i + d_row < len(board) and 0 <= j + d_col < len(board[i]):
            i += d_row
            j += d_col
            if board[i][j] == 'B' or board[i][j] == 'Q':
                return True
            if board[i][j] != '.':
                break
    return False

def q_atk(board, k_p):
    return r_atk(board, k_p) or b_atk(board, k_p)

def main():
    board = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', 'Q', '.', '.', '.', '.'],
        ['.', '.', '.', 'K', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
    ]
    checkmate(board)

if __name__ == "__main__":
    main()
