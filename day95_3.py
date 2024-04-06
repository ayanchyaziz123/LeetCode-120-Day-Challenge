from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # Sort the array in non-decreasing order
        arr.sort()
        
        # Calculate the number of elements to remove from both ends
        percentage_to_remove = (5 * len(arr)) // 100
        
        # Initialize variables to keep track of the sum and count of elements to calculate mean
        total_sum = 0
        count = 0
        
        # Iterate over the array, excluding the elements from the ends
        for i in range(percentage_to_remove, len(arr) - percentage_to_remove):
            # Add the current element to the sum
            total_sum += arr[i]
            # Increment the count of elements
            count += 1
        
        # Calculate the mean and return it
        return total_sum / count
