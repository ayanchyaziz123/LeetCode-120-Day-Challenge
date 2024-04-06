from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Initialize index variable to store the index of target if found
        ind = -1
        
        # Initialize pointers for binary search
        left = 0
        right = len(nums) - 1
        
        # Perform binary search to find the index of target
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ind = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        # If target not found, return [-1, -1]
        if ind == -1:
            return [-1, -1]
        
        # Initialize variables to store left and right boundaries
        left_ans = ind
        right_ans = ind
        
        # Update left boundary
        while left_ans - 1 >= 0 and nums[left_ans - 1] == target:
            left_ans -= 1
        
        # Update right boundary
        while right_ans + 1 < len(nums) and nums[right_ans + 1] == target:
            right_ans += 1
        
        # Return the left and right boundaries
        return [left_ans, right_ans]
