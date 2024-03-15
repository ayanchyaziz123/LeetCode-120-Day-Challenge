class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = 0  # Initialize a counter for the number of zeros encountered
        ple = 0  # Store the index of the position of the zero encountered
        val = 1  # Initialize a variable to calculate product of all non-zero elements
        # Loop through each element in the array
        for i, num in enumerate(nums):
            # Check if the current element is zero
            if num == 0:
                cnt += 1  # Increment the zero count
                ple = i   # Store the index of the position of the zero
            else:
                val *= num  # Calculate the product of all non-zero elements
        n = len(nums)  # Length of the input array
        res = [0] * n  # Initialize result array with zeros

        # If there are more than one zero, the result would be all zeros
        if cnt > 1:
            return res
        # If there's exactly one zero, set the product to the index of that zero
        if cnt == 1:
            res[ple] = val
            return res
        # Calculate the result for each element by dividing the product of all elements by the corresponding element
        for i in range(n):
            res[i] = (val) // nums[i]
        return res
