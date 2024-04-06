from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Initialize hashmap with 0: -1 to handle cases starting from index 0
        count_map = {0: -1}
        count = 0
        max_length = 0

        # Enumerate over nums to get both index and value
        for current_index, num in enumerate(nums):
            # Update count based on current element
            if num == 0:
                count -= 1
            else:
                count += 1

            # If this count has been seen, calculate the potential max_length
            if count in count_map:
                subarray_length = current_index - count_map[count]
                max_length = max(max_length, subarray_length)
            else:
                # Only set the count in the hashmap if it's not already present
                count_map[count] = current_index

        return max_length
