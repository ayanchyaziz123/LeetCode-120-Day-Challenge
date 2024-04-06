from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the list
        for i in range(n):  # Iterate through each element in the list
            ind = abs(nums[i]) - 1  # Get the index by taking the absolute value of the current number and subtracting 1
            if nums[ind] < 0:  # If the number at the calculated index is negative
                return abs(nums[i])  # This indicates that the number is a duplicate, so return it (using its absolute value)
            nums[ind] = -nums[ind]  # Mark the number at the calculated index as negative to indicate it has been visited
