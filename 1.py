from typing import List
from math import pow, floor

class Solution:
    def oddEven2(self, n: int) -> List[int]:
        p1 = 0
        p2 = 0
        for i in range(1, n+1):
            if i % 2 == 0:
                p1+=i
            else:
                p2+=i
        return [p2, p1] 
    def oddEven(self, n: int) -> List[int]:
        total_even, total_odd = 0, 0
        if n % 2 == 0:
            total_even = n//2
            total_odd = n//2
        else:
            total_even = n//2
            total_odd = n//2 + 1 
        odd_sum = floor(pow(total_odd, 2))
        even_sum = total_even * (total_even + 1)
        return [odd_sum, even_sum]
print(Solution().oddEven(123456788))
