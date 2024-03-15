from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Initialize the answer to 0
        ans = 0
        # Initialize prefix sum to 0
        prefix_sum = 0
        # Initialize a dictionary to keep track of prefix sums encountered
        prefix_sums = defaultdict(int)
        
        # Iterate through each number in the nums array
        for num in nums:
            # Update the current prefix sum with the current number
            prefix_sum += num
            # Calculate the complement sum needed to reach the goal
            complement_sum = prefix_sum - goal
            # If the complement sum exists in the prefix_sums dictionary,
            # it means there's a subarray ending at the current index
            # which sums up to the goal. Increment ans by the count of such subarrays.
            ans += prefix_sums[complement_sum]
            # Increment the count of the current prefix sum in the prefix_sums dictionary
            prefix_sums[prefix_sum] += 1
            # If the current prefix sum equals the goal, increment ans by 1
            if prefix_sum == goal:
                ans += 1
        
        # Return the total count of subarrays that sum up to the goal
        return ans
