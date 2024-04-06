from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # Iterate until the original value is not in nums
        while original in nums:
            # Double the original value
            original *= 2
        
        # Return the final value after all doublings
        return original
