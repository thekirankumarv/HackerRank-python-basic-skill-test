import math
import os
import random
import re
import sys


def numCells(grid):
    n = len(grid)
    m = len(grid[0])

    count = 0

    for i in range(n):
        for j in range(m):
            cell_value = grid[i][j]
            is_dominant = True

            # Check all 8 neighbors of the cell
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue

                    ni = i + dx
                    nj = j + dy

                    # Ignore cells outside the grid boundaries
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] >= cell_value:
                        is_dominant = False
                        break

                if not is_dominant:
                    break

            if is_dominant:
                count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
