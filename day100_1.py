from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Create a frequency array to count occurrences of positive numbers
        freq = [0] * (len(nums) + 1)
        
        # Count occurrences of positive numbers in the input array
        for num in nums:
            if num <= len(nums) and num > 0:
                freq[num] += 1
        
        # Print the frequency array for debugging purposes
        print(freq)
        
        # Find the first missing positive integer
        for i in range(1, len(freq)):
            if freq[i] == 0:
                return i
        
        # If all positive integers from 1 to len(nums) are present, return len(nums)+1
        return len(nums) + 1
