from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])  # Get the dimensions of the grid
        
        # Flatten the grid into a 1D list
        flattened_grid = [num for row in grid for num in row]
        
        # Perform the shift operation k times
        for _ in range(k):
            # Shift the last element to the beginning
            last_element = flattened_grid.pop()
            flattened_grid.insert(0, last_element)
        
        # Reshape the flattened list back into a 2D grid
        shifted_grid = []
        for i in range(m):
            row = flattened_grid[i * n: (i + 1) * n]
            shifted_grid.append(row)
        
        return shifted_grid
