from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arr = []  # Initialize an empty list to store the unique numbers
        res = 0  # Initialize a variable to store the result
        n = len(nums)  # Get the length of the input list
        for i in range(n - 1, -1, -1):  # Iterate through the input list in reverse order
            if len(arr) == k:  # If the number of unique numbers in arr equals k
                return res  # Return the current result
            if nums[i] not in arr:  # If the current number is not already in arr
                if nums[i] <= k:  # If the current number is less than or equal to k
                    arr.append(nums[i])  # Add the current number to arr
            res += 1  # Increment the result count
        return res  # Return the final result
