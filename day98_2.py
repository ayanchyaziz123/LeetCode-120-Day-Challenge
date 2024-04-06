from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        special_count = 0
        
        # Iterate through each cell in the matrix
        for i in range(rows):
            for j in range(cols):
                # Check if current cell is 1
                if mat[i][j] == 1:
                    # Check if all other elements in row i are 0
                    if sum(mat[i]) != 1:
                        continue
                    # Check if all other elements in column j are 0
                    if sum(mat[row][j] for row in range(rows)) != 1:
                        continue
                    # If both conditions are met, increment special_count
                    special_count += 1
        
        return special_count
