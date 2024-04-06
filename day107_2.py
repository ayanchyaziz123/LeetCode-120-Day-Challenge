from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], d: int) -> int:
        n = len(timeSeries)  # Length of the time series
        res = 0  # Initialize the result
        
        # Iterate through each time point except the last one
        for i in range(n-1):
            # If the current time point + duration overlaps with the next time point
            if (timeSeries[i] + d) >= timeSeries[i+1]:
                res += (timeSeries[i+1] - timeSeries[i])  # Add the duration of overlap
            else:
                res += (timeSeries[i] + d - timeSeries[i])  # Add the full duration
        
        # Add the duration of the last time point
        res += (timeSeries[n-1] + d - timeSeries[n-1])
        
        return res  # Return the total duration

# Example usage:
sol = Solution()
timeSeries = [1, 4, 7]
d = 3
print(sol.findPoisonedDuration(timeSeries, d))  # Output: 6
