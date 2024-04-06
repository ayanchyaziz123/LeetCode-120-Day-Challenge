from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)  # Get the length of the input list
        res = 0  # Initialize a variable to store the result
        for i in range(n):  # Loop through each element of the input list
            for j in range(i + 1, n):  # Loop through each element after the current element
                for k in range(j + 1, n):  # Loop through each element after the j-th element
                    # Check if the absolute differences between elements at indices i, j, and k are within the limits a, b, and c
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res += 1  # If the conditions are met, increment the result count
        return res  # Return the final result
