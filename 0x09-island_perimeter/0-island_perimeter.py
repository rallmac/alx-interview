#!/usr/bin/python3
"""This python code measures the perimeter of an island
"""


def island_perimeter(grid):
    """this is the grid function, it returns the perimeter
    of the island described in the grid input
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # if it's land
                # check for directions
                if i == 0 or grid[i - 1][j] == 0:  # edge or water
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
