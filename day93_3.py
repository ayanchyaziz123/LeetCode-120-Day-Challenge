from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize the current minimum as the last element of the list
        cur = nums[-1]
        
        # Initialize the pointers for binary search
        low = 0
        high = len(nums) - 1

        # Binary search
        while low <= high:
            mid = (low + high) // 2  # Calculate the middle index
            
            if nums[mid] <= cur:
                # If the element at mid is less than or equal to current minimum,
                # update the current minimum and search in the left half
                cur = nums[mid]
                high = mid - 1
            else:
                # If the element at mid is greater than current minimum,
                # search in the right half
                low = mid + 1
        
        # Return the current minimum found
        return cur

# Example usage:
solution = Solution()
print(solution.findMin([3, 4, 5, 1, 2]))  # Output: 1
print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
