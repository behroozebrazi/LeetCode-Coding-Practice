# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        result = 1
        left = right = 0
        points.sort(key=lambda x: x[1])

        for right in range(len(points)):
            if points[left][1] < points[right][0]:
                result += 1
                left = right

        return result