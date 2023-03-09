#!/usr/bin/python3
"""N-queen"""

import sys


def n_queen():
    col = set()
    nagDig = set() # r - c
    posDig = set() # r + c
    res = []
    try:
        num = int(sys.argv[1])
    except IndexError:
        print("Usage: nqueens N")
        exit(1)
    except ValueError:
        print("N must be a number")
        exit(1)
    
    if num < 4:
        print("N must be at least 4")
        exit(1)

    board = [["."] * num for i in range(num)]

    def backtrack(r):
        if r == num:
            res.append(board)
            return
        
        for c in range(num):
            if c in col or (r + c) in posDig or (r - c) in posDig:
                continue

            col.add(r)
            posDig.add(r + c)
            nagDig.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(r)
            posDig.remove(r + c)
            nagDig.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res


    


ans = n_queen()
print(ans)