# https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = localMaxSum = -10000

        for num in nums:
            localMaxSum = num if localMaxSum <= 0 else localMaxSum + num

            if maxSum < localMaxSum:
                maxSum = localMaxSum

        return maxSum



# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSum = localMaxSum = -10000

#         for num in nums:
#             localMaxSum = max(num, localMaxSum + num)
#             maxSum = max(maxSum, localMaxSum)

#         return maxSum