from typing import List

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        prfx_sum = []  # List to store prefix sums
        ple = 0  # Prefix sum accumulator
        for num in nums:
            ple += num  # Incrementally calculate prefix sum
            prfx_sum.append(ple)  # Append the prefix sum to the list

        res = 0  # Initialize result counter to count occurrences of 0 prefix sum
        for num in prfx_sum:  # Iterate through the prefix sum list
            if num == 0:  # If prefix sum is 0
                res += 1  # Increment the result counter

        return res  # Return the count of 0 prefix sums

# Example usage:
solution = Solution()

# Example 1
nums1 = [0, 1, -1, 0]
print(solution.returnToBoundaryCount(nums1))  # Output: 3 (Three 0 prefix sums)

# Example 2
nums2 = [0, 0, 0, 0, 0]
print(solution.returnToBoundaryCount(nums2))  # Output: 5 (Five 0 prefix sums)
