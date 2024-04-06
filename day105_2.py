from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the size of the board (number of rows and columns)
        row_size = len(board)
        col_size = len(board[0])
        
        # Create a 2D array to keep track of visited cells
        visited = [[0] * col_size for _ in range(row_size)]
        
        # Define a depth-first search function to search for the word on the board
        def dfs(r, c, ind):
            # If the entire word has been found, return True
            if ind == len(word):
                return True
            
            # Check if the current cell is out of bounds, already visited, or doesn't match the current character in the word
            if r not in range(row_size) or c not in range(col_size) or visited[r][c] or board[r][c] != word[ind]:
                return False
            
            # Mark the current cell as visited
            visited[r][c] = 1
            
            # Recursively search in all four directions (up, down, left, right)
            result = dfs(r+1, c, ind+1) or dfs(r, c+1, ind+1) or dfs(r-1, c, ind+1) or dfs(r, c-1, ind+1)
            
            # Mark the current cell as not visited for other paths to explore
            visited[r][c] = 0
            
            return result
        
        # Iterate through each cell on the board and start the DFS search
        for r in range(row_size):
            for c in range(col_size):
                if dfs(r, c, 0):
                    return True
        
        # If no path is found, return False
        return False
