from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:  # Ensure start is always less than destination
            start, destination = destination, start
        # Calculate clockwise distance
        clockwise_distance = sum(distance[start:destination])
        # Calculate counterclockwise distance
        counterclockwise_distance = sum(distance[:start]) + sum(distance[destination:])
        # Return the minimum of the two distances
        return min(clockwise_distance, counterclockwise_distance)

# Example usage
sol = Solution()
distance = [1, 2, 3, 4]
start = 0
destination = 2
print(sol.distanceBetweenBusStops(distance, start, destination))  # Output: 3

distance = [1, 2, 3, 4]
start = 0
destination = 3
print(sol.distanceBetweenBusStops(distance, start, destination))  # Output: 4
