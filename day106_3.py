class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0  # Initialize the maximum depth to 0
        current_depth = 0  # Initialize the current depth to 0
        
        # Loop through each character in the string
        for char in s:
            if char == '(':  # If the character is an opening parenthesis
                current_depth += 1  # Increment the current depth
                max_depth = max(max_depth, current_depth)  # Update the maximum depth if needed
            elif char == ')':  # If the character is a closing parenthesis
                current_depth -= 1  # Decrement the current depth
        
        return max_depth  # Return the maximum depth

# Create an instance of the Solution class
solution = Solution()

# Example 1
s1 = "(1+(2*3)+((8)/4))+1"
print(solution.maxDepth(s1))  # Output: 3

# Example 2
s2 = "(1)+((2))+(((3)))"
print(solution.maxDepth(s2))  # Output: 3
