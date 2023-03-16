#!/usr/bin/python3
"""rotate 2d matrix"""


def rotate_2d_matrix(matrix):
    N = len(matrix)
    # Consider all squares one by one
    for x in range(0, int(N / 2)):

        # Consider elements in group
        # of 4 in current square
        for y in range(x, N-x-1):

            # store current cell in temp variable
            temp = matrix[x][y]

            # move values from right to top
            matrix[x][y] = matrix[y][N-1-x]

            # move values from bottom to right
            matrix[y][N-1-x] = matrix[N-1-x][N-1-y]

            # move values from left to bottom
            matrix[N-1-x][N-1-y] = matrix[N-1-y][x]

            # assign temp to left
            matrix[N-1-y][x] = temp
