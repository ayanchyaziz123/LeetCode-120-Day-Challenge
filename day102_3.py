class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # Initialize variables to store the sum of elements on the left and right side of the array
        left_sum = 0
        right_sum = 0
        
        # Get the length of the array
        n = len(nums)
        
        # Calculate the initial sum of all elements in the array for the right_sum
        for num in nums:
            right_sum += num
        
        # Initialize the result variable and the minimum difference variable
        res = 0
        mn = float('inf')
        
        # Iterate through the array
        for i in range(n):
            # Add the current element to the left_sum
            left_sum += nums[i]
            
            # Subtract the current element from the right_sum
            right_sum -= nums[i]
            
            # Calculate the number of elements on the right side
            x = (n - (i + 1))
            
            # Calculate the average of the left_sum
            ls = left_sum // (i + 1)
            
            # Calculate the average of the right_sum if there are elements on the right side,
            # otherwise set it to 0
            if x != 0:
                rs = right_sum // x
            else:
                rs = 0
            
            # Print the left_sum and right_sum for debugging purposes
            print(ls, rs)
            
            # Update the result and minimum difference if the absolute difference of averages is smaller
            if abs(ls - rs) < mn:
                res = i
                mn = abs(ls - rs)
        
        # Return the index where the minimum average difference occurs
        return res
