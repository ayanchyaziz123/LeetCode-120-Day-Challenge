from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        # Check rows
        for row in matrix:
            if sorted(row) != list(range(1, n + 1)):
                return False

        # Check columns
        for j in range(n):
            column = [matrix[i][j] for i in range(n)]
            if sorted(column) != list(range(1, n + 1)):
                return False

        return True

# Example usage:
solution = Solution()
matrix1 = [[1,2,3],[3,1,2],[2,3,1]]
print(solution.checkValid(matrix1))  # Output: True

matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
print(solution.checkValid(matrix2))  # Output: False
