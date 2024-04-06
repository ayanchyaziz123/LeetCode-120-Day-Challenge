from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the points based on their start positions
        points.sort()
        
        # Initialize the result with the total number of points
        res = len(points)
        
        # Initialize the previous point with the first point
        prev = points[0]
        
        # Iterate through all points starting from the second one
        for i in range(1, len(points)):
            # Current point
            curr = points[i]
            
            # If the start of the current point is less than or equal to the end of the previous point
            if curr[0] <= prev[1]:
                # The current point can be covered by the previous arrow, so decrement the result
                res -= 1
                
                # Update the previous point's end to be the minimum of current and previous ends
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                # No overlap between current and previous points, update the previous point
                prev = curr
        
        # Return the result
        return res

# Example usage:
solution = Solution()
print(solution.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))  # Output: 2
print(solution.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))    # Output: 4
