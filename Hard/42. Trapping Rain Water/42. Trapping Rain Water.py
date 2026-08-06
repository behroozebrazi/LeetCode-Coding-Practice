# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]

                left += 1

            else:

                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]

                right -= 1

        return water


# class Solution:
#     def trap(self, height: List[int]) -> int:

#         n = len(height)
#         maxHeight = [0] * n
#         water = 0

#         for i, h in enumerate(height):
#             maxHeight[i] = max(maxHeight[i - 1] , h)

#         trapMaxHeight = 0
#         for i in range(n - 1, -1, -1):
#             trapMaxHeight = max(height[i], trapMaxHeight)
#             maxHeight[i] = min(maxHeight[i] , trapMaxHeight)
#             water += maxHeight[i] - height[i]

#         return water