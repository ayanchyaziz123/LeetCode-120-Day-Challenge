class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Initialize variables to store the sum of elements on the left and right side of the array
        left_sum = 0
        right_sum = 0
        
        # Get the length of the array
        n = len(nums)
        
        # Calculate the initial sum of all elements in the array for the right_sum
        for i in range(n):
            right_sum += nums[i]
        
        # Initialize the result counter
        res = 0
        
        # Iterate through the array
        for i in range(n-1):
            # Update the right_sum by subtracting the current element from it
            right_sum -= nums[i]
            
            # Add the current element to the left_sum
            left_sum += nums[i]
            
            # Check if the left_sum is greater than or equal to the right_sum
            if left_sum >= right_sum:
                # Increment the result counter
                res += 1
        
        # Return the total count of ways to split the array
        return res
