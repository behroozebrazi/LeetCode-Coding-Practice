# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        localMaxWater = 0
        maxWater = 0

        while left < right:
            diff = height[left] - height[right]

            if diff > 0:
                localMaxWater = (right - left) *  height[right]
                right -= 1

            else:
                localMaxWater = (right - left) *  height[left]
                left += 1

            if maxWater < localMaxWater:
                maxWater = localMaxWater

        return maxWater