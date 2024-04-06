from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Iterate through each element in the array
        for i in range(len(arr)):
            # Compare the current element with all other elements in the array
            for j in range(len(arr)):
                # Ensure that the indices are not the same and check if the current element is twice the other element
                if i != j and arr[i] == 2 * arr[j]:
                    # If the condition is satisfied, return True indicating that such a pair exists
                    return True
        
        # If no such pair is found after checking all combinations, return False
        return False
