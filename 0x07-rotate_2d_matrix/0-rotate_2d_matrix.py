#!/usr/bin/python3
"""rotate 2d matrix"""


def rotate_2d_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):

            # swapping matrix[i][j] and matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse
    for i in range(len(matrix)):
        matrix[i].reverse()
