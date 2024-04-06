from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Find the maximum element in the array
        mx = max(nums)
        # Initialize a counter for the maximum element occurrences
        cnt = 0
        # Initialize the start index for the sliding window
        start = 0
        # Get the length of the array
        n = len(nums)
        # Initialize the result counter
        res = 0
        
        # Iterate through the array
        for i in range(n):
            # Increment the counter if the current element equals the maximum element
            if nums[i] == mx:
                cnt += 1
            # Slide the window while the count of maximum elements is greater than or equal to k
            while cnt >= k:
                # Add the number of subarrays ending at the current index to the result
                res += (n - i)
                # Move the start of the window forward and decrement the counter if the element at start is the maximum
                if nums[start] == mx:
                    cnt -= 1
                start += 1
                
        # Return the total count of subarrays satisfying the condition
        return res
