from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Memoization dictionary to store already calculated results
        memo = {}
        
        def solve(ind):
            # If the result for this index is already calculated, return it from memo
            if ind in memo:
                return memo[ind]
            
            # If the current index is at the end or beyond, return True
            if ind >= len(nums) - 1:
                return True
            
            # If the current element is 0, it's impossible to move forward
            if nums[ind] == 0:
                return False
            
            # If jumping from the current index reaches the end or beyond, return True
            if (ind + nums[ind]) >= (len(nums) - 1):
                return True
            
            # Try jumping from the current index to all possible reachable indices
            ans = False
            for i in range(1, nums[ind] + 1):
                ans = ans or solve(ind + i)  # Try jumping and update the answer
                
            # Store the result in memo for future reference
            memo[ind] = ans
            return memo[ind]
        
        # Start solving from index 0
        return solve(0)

# Example usage:
solution = Solution()
print(solution.canJump([2,3,1,1,4]))  # Output: True
print(solution.canJump([3,2,1,0,4]))  # Output: False
