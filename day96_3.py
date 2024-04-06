from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # Sort the given list of numbers
        nums.sort()
        
        # Initialize the maximum gap
        mx = 0
        
        # Iterate through the sorted list
        for i in range(len(nums)-1):
            # Calculate the difference between consecutive elements
            gap = nums[i+1] - nums[i]
            
            # Update the maximum gap if the current gap is larger
            mx = max(mx, gap)
        
        # Return the maximum gap
        return mx
