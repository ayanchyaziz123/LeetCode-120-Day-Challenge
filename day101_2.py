class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        # If k is less than or equal to 1, it's not possible to have a product less than k
        if k <= 1:
            return 0

        count = 0        # Variable to store the count of subarrays with product less than k
        product = 1      # Variable to store the current product of elements in the subarray
        left = 0         # Pointer for the start of the current subarray

        # Iterate through the array with a sliding window approach
        for right in range(len(nums)):
            product *= nums[right]  # Update the product by multiplying with the current element
            # Adjust the subarray to maintain the product less than k
            while product >= k:
                product /= nums[left]  # Remove the leftmost element from the product
                left += 1               # Move the left pointer to the right
            # Update the count with the number of valid subarrays ending at the current position
            count += right - left + 1

        return count  # Return the total count of subarrays with product less than k

# Test the solution with the given example
nums = [10, 5, 2, 6]
k = 100
solution = Solution()
print(solution.numSubarrayProductLessThanK(nums, k))  # Output: 8
