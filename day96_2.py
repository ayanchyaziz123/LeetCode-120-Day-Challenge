from typing import List
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        # Initialize the maximum consecutive count
        mx = 0
        
        # Append the bottom and top values to the special list
        special.append(bottom)
        special.append(top)
        
        # Sort the special list in ascending order
        special.sort()
        
        # Iterate through the special list
        for i in range(1, len(special)):
            # Calculate the gap between consecutive elements
            gap = special[i] - special[i-1]
            
            # If the gap is greater than 1, it means there's a space between consecutive elements
            if gap > 1:
                # If it's the first or last element, just update the maximum consecutive count
                if i == len(special) - 1 or i == 1:
                    mx = max(mx, gap)
                else:
                    # If it's neither the first nor the last element, consider the space between
                    # the current and previous element, and update the maximum consecutive count
                    mx = max(mx, gap - 1)
        
        return mx
