from typing import List
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # Initialize an empty set to store unique elements that appear in at least two lists
        res = set()
        
        # Iterate through the elements in nums1
        for num1 in nums1:
            # Check if the current element exists in nums2 or nums3
            if num1 in nums2 or num1 in nums3:
                # If it does, add it to the result set
                res.add(num1)
        
        # Iterate through the elements in nums2
        for num2 in nums2:
            # Check if the current element exists in nums1 or nums3
            if num2 in nums1 or num2 in nums3:
                # If it does, add it to the result set
                res.add(num2)
        
        # Iterate through the elements in nums3
        for num3 in nums3:
            # Check if the current element exists in nums1 or nums2
            if num3 in nums1 or num3 in nums2:
                # If it does, add it to the result set
                res.add(num3)
        
        # Return the set containing unique elements that appear in at least two lists
        return res
