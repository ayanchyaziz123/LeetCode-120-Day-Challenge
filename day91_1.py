from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Dictionary to store frequency of each number
        freq = {}
        
        # Calculate the target count of distinct numbers
        n = len(nums) // 2
        
        # Count frequency of each number in nums
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Count of distinct numbers that appear more than once
        cnt = 0
        
        # Iterate over frequency dictionary
        for key in freq:
            # If a number appears less than 2 times, array cannot be divided
            if freq[key] < 2:
                return False
            # If a number appears more than 2 times, count the number of times it can be divided
            if freq[key] > 2:
                cnt += (freq[key] // 2)
            else:
                cnt += 1
        
        # If the count of distinct numbers that can be divided is equal to the target count, return True
        if cnt == n:
            return True
        
        # Otherwise, return False
        return False
