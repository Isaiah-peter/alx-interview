#!/usr/bin/python3
"""0x0A. Prime Game
"""


def island_perimeter(grid):
    """prime game
    """
    p = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x]:
                if x == 0 or not grid[y][x - 1]:
                    p += 1
                if x == len(grid[0]) - 1 or not grid[y][x + 1]:
                    p += 1
                if y == 0 or not grid[y - 1][x]:
                    p += 1
                if y == len(grid) - 1 or not grid[y + 1][x]:
                    p += 1
    return p
