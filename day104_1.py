from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        # [1] Storage for indices of the last encountered
        #     types of numbers (minK, maxK, and out-of-range)
        last_out = -1  # Index of the last out-of-range number
        last_min = -1  # Index of the last minK number
        last_max = -1  # Index of the last maxK number
        
        count = 0  # Counter for the number of valid subarrays
        
        for i, n in enumerate(nums):
            
            # Check if the current number is within the range [minK, maxK]
            if minK <= n <= maxK: 
                # Update the last_min and last_max indices if applicable
                if n == minK:
                    last_min = i
                if n == maxK:
                    last_max = i
                # Calculate the length of the subarray and add it to the count
                count += max(min(last_min, last_max) - last_out, 0)
            else:
                # Update the last_out index to the current index
                last_out = i
            
        return count
