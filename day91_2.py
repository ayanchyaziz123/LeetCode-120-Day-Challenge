from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # Initialize two arrays to store alternate elements
        arr1 = []
        arr2 = []
        
        # Initialize variables to store current values
        val1 = nums[0]
        val2 = nums[1]
        
        # Add initial values to respective arrays
        arr1.append(val1)
        arr2.append(val2)
        
        # Iterate through the remaining elements in nums
        for i in range(2, len(nums)):
            # Compare current values and append to the appropriate array
            if val1 < val2:
                val2 = nums[i]
                arr2.append(val2)
            else:
                val1 = nums[i]
                arr1.append(val1)
        
        # Concatenate the two arrays and return the result
        return arr1 + arr2
