from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Initialize a dictionary to store the frequency of elements in arr1
        freq = {}
        # Initialize a temporary list to store elements in arr1 not present in arr2
        temp = []

        # Iterate through arr1 to count frequency and populate temp
        for num in arr1:
            # If num not in arr2, append it to temp
            if num not in arr2:
                temp.append(num)
            # Update frequency count for num
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Initialize the result list
        res = []

        # Sort elements in temp
        temp.sort()

        # Iterate through arr2 to populate res with elements and their frequencies
        for num in arr2:
            # Get the frequency of num from the freq dictionary
            n = freq[num]
            # Append num to res n times
            for i in range(n):
                res.append(num)

        # Return the concatenated result of res and temp
        return res + temp
