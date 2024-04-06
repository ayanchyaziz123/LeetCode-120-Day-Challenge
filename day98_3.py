from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # Calculate the prefix sum of the entire array
        prefix_sum = sum(nums)
        left_sum = 0
        
        # Iterate through each element in the array
        for i in range(len(nums)):
            # Subtract the current element from the prefix sum
            prefix_sum -= nums[i]
            
            # If prefix_sum equals left_sum, return the current index
            if prefix_sum == left_sum:
                return i
            
            # Update left_sum by adding the current element
            left_sum += nums[i]
        
        # If no middle index is found, return -1
        return -1
