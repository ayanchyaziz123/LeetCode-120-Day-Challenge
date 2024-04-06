class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)  # Length of the input array
        res = 0  # Initialize the result
        
        # Iterate over all possible subarrays
        for i in range(n):  # Start index of the subarray
            for j in range(i, n):  # End index of the subarray
                if (j - i + 1) % 2 == 0:  # Check if the length of the subarray is odd
                    continue  # Skip even length subarrays
                
                # Calculate the sum of the elements in the current subarray
                subarray_sum = sum(arr[i:j+1])
                
                # Add the sum of the current subarray to the result
                res += subarray_sum
        
        return res  # Return the total sum of odd length subarrays
