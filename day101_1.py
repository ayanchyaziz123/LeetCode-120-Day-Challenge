from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Initialize variables
        start = 0  # Pointer for the start of the subarray
        res = 0    # Length of the current subarray
        mx = 0     # Maximum length of subarrays with sum less than or equal to k
        freq = {}  # Dictionary to store the frequency of elements in the subarray

        # Iterate through the array
        for i in range(len(nums)):
            # Increment the length of the subarray
            res += 1

            # Update the frequency of the current element
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

            # Adjust the subarray to meet the sum constraint
            while start < i and freq[nums[i]] > k:
                freq[nums[start]] -= 1
                start += 1
                res -= 1

            # Update the maximum length of subarrays
            mx = max(mx, res)

        return mx  # Return the maximum length of subarrays satisfying the condition
