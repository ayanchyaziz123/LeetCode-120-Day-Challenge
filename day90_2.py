from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Initialize index i to track current positive integer
        i = 0
        
        # Iterate until we find the kth missing positive integer
        while k > 0:
            # Increment current positive integer
            i += 1
            
            # If the current positive integer is not in the array,
            # decrement k (indicating we found a missing positive integer)
            if i not in arr:
                k -= 1
        
        # Return the current positive integer when k becomes 0
        return i
