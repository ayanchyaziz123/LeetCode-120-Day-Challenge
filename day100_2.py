from typing import List
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # Find the maximum and minimum values in the array
        mx = max(nums)  # Maximum value
        mn = min(nums)  # Minimum value
        
        # Calculate the result by subtracting k from the maximum and adding k to the minimum
        # This effectively shrinks the range to reduce the difference between the maximum and minimum values
        res = (mx - k) - (mn + k)
        
        # Check if the result is less than or equal to 0
        if res <= 0:
            return 0  # If the result is non-positive, return 0
        
        # If the result is positive, return the result
        else:
            return res
