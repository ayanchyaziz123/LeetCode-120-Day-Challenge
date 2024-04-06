from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = 0
        count = 0
        sum_freq = {0: 1}  # Dictionary to store frequency of prefix sums
        
        for i in range(n):
            prefix_sum += nums[i]
            # Check if prefix_sum - k exists in the dictionary, if yes, increment count
            if prefix_sum - k in sum_freq:
                count += sum_freq[prefix_sum - k]
            # Increment the frequency of prefix_sum
            sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1
        
        return count