from typing import List

class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        # If no flowers need to be placed, return True
        if n == 0:
            return True
        
        # If there's only one plot and it's empty, we can place a flower
        if len(nums) == 1 and nums[0] == 0:
            return True
        
        # If the first two plots are empty, place a flower in the first plot
        if len(nums) > 1 and nums[0] == 0 and nums[1] == 0:
            nums[0] = 1
            n -= 1
        
        # If the last two plots are empty, place a flower in the last plot
        if len(nums) > 1 and nums[-1] == 0 and nums[-2] == 0:
            nums[-1] = 1
            n -= 1
        
        # Loop through the plots to check if we can place flowers
        for i in range(1, len(nums) - 1):
            if nums[i] != 1 and (nums[i - 1] == 0 and nums[i + 1] == 0):
                nums[i] = 1
                n -= 1
        
        # If we have placed all required flowers, return True
        if n <= 0:
            return True
        else:
            return False
