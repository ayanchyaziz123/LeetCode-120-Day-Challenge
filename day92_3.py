from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged_intervals = []  # List to store merged intervals
        i = 0  # Initialize index for traversing intervals list
        num_intervals = len(intervals)  # Get the length of intervals list

        # Add all intervals that end before the new interval starts
        while i < num_intervals and intervals[i][1] < newInterval[0]:
            merged_intervals.append(intervals[i])  # Append non-overlapping intervals
            i += 1

        # Merge intervals that overlap with the new interval
        while i < num_intervals and intervals[i][0] <= newInterval[1]:
            # Update newInterval to merge overlapping intervals
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        merged_intervals.append(newInterval)  # Append the merged interval

        # Add remaining intervals
        while i < num_intervals:
            merged_intervals.append(intervals[i])  # Append non-overlapping intervals
            i += 1

        return merged_intervals  # Return the merged intervals
