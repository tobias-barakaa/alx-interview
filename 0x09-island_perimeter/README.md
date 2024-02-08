# Island Perimeter Algorithm

## Overview
The Island Perimeter algorithm is a problem-solving technique used in computer science to determine the perimeter of an island within a grid. This algorithm is commonly encountered in questions related to grids or matrices, where the goal is to calculate the perimeter of a contiguous group of cells representing land.

## Problem Statement
Given a grid representing a map where 0 represents water and 1 represents land, the task is to calculate the perimeter of the island within the grid. An island in this context refers to a contiguous group of cells with a value of 1, surrounded by water (cells with a value of 0).

## Algorithm
The algorithm traverses the grid cell by cell. For each cell with a value of 1 (indicating land), it examines its adjacent cells (up, down, left, and right) to determine if there's water. If water is found adjacent to the current cell, the algorithm increments the perimeter count by 1 for that side.

Special attention should be given to the boundary cells of the grid. If an island reaches the boundary of the grid, those edges should be counted as part of the perimeter as well.

Finally, the algorithm returns the total perimeter of the island.

## Pseudocode
```python
def islandPerimeter(grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
                    
    return perimeter

