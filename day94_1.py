from queue import PriorityQueue
from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Initialize a priority queue
        pq = PriorityQueue()
        
        # Iterate through each asteroid
        for asteroid in asteroids:
            # If the current mass is sufficient to destroy the asteroid, consume it
            if mass >= asteroid:
                mass += asteroid
            else:
                # If not enough mass, add the asteroid to the priority queue
                pq.put(asteroid)
            
            # Process asteroids in the priority queue as long as they can be destroyed
            while not pq.empty() and pq.queue[0] <= mass:
                mass += pq.get()
        
        # If the priority queue is empty, all asteroids are destroyed
        if pq.empty():
            return True
        else:
            return False
