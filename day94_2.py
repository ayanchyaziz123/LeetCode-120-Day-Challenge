from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            # If the stack is not empty and the top asteroid is moving right and the current asteroid is moving left
            while stack and stack[-1] > 0 and asteroid < 0:
                # Handle collision between asteroids
                if stack[-1] < abs(asteroid):
                    stack.pop()  # Top asteroid destroyed
                elif stack[-1] == abs(asteroid):
                    stack.pop()  # Both asteroids destroyed
                    break  # Break the inner while loop since the current asteroid is destroyed
                else:
                    break  # Current asteroid destroyed, break the inner while loop
                
            else:
                # No collision, push the current asteroid onto the stack
                stack.append(asteroid)
        
        return stack

# Example usage:
solution = Solution()
print(solution.asteroidCollision([5, 10, -5]))  # Output: [5, 10]
print(solution.asteroidCollision([8, -8]))     # Output: []
