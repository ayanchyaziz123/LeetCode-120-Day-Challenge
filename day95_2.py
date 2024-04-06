from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # If there is only one task, no idle time is needed
        if len(tasks) == 1:
            return 1
        
        # Count the occurrences of each task
        task_count = Counter(tasks)
        
        # Find the task with the maximum occurrences
        max_occurrences = max(task_count.values())
        
        # Calculate the total time required
        total_time = (max_occurrences - 1) * (n + 1) + 1
        
        # Iterate over the values in the counter
        for count in task_count.values():
            if count == max_occurrences:
                # Increment the total time for tasks with the maximum occurrences
                total_time += 1
        
        # The minimum time required is either the calculated total time or the total number of tasks
        return max(total_time - 1, len(tasks))
