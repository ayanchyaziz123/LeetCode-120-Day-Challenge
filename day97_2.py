from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Calculate the size of the grid
        n = len(grid) * len(grid[0])
        
        # Initialize a frequency array to store the count of each number
        freq = [0] * (n + 1)
        
        # Iterate through the grid and update the frequency array
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                freq[grid[r][c]] += 1
        
        # Initialize variables to store the missing and repeated values
        res1 = 0
        res2 = 0
        
        # Iterate through the frequency array to find the missing and repeated values
        for i in range(1, n + 1):
            if freq[i] == 2:
                res1 = i  # Repeated value found
            if freq[i] == 0:
                res2 = i  # Missing value found
        
        # Return the list containing the repeated and missing values
        return [res1, res2]
