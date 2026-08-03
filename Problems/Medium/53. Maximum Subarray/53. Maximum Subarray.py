# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = maxSumLocal = -10000

        for num in nums:
            maxSumLocal = max(num, maxSumLocal + num)
            maxSum = max(maxSum, maxSumLocal)

        return maxSum