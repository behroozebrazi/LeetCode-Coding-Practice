# https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        start, end = newInterval

        for s, e in intervals:

            # Current interval is completely before new interval
            if e < start:
                result.append([s, e])

            # Current interval is completely after new interval
            elif end < s:
                result.append([start, end])
                start, end = s, e

            # Overlapping intervals -> merge
            else:
                start = min(start, s)
                end = max(end, e)

        result.append([start, end])

        return result