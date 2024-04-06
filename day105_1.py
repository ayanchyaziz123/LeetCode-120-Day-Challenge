from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Sort the input list of numbers
        nums.sort()
        
        # Initialize variables
        ind = 0
        n = len(nums)
        
        # Find the index of the last negative number or 0
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            ind = i
        
        # If all numbers are non-positive, return the last number
        if ind == n-1:
            return nums[ind]
        
        # If the absolute value of the current number is equal to the next number, return the next number
        if abs(nums[ind]) == nums[ind+1]:
            return nums[ind+1]
        
        # If the absolute value of the current number is less than the next number, return the current number
        if abs(nums[ind]) < (nums[ind+1]):
            return nums[ind]
        # If the absolute value of the current number is greater than or equal to the next number, return the next number
        else:
            return nums[ind+1]
