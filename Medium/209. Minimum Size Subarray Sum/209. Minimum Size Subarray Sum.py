# https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minLength = len(nums) + 1
        sumNums = 0
        left = 0

        for right, num in enumerate(nums):
            sumNums += num

            while sumNums >= target:
                minLength = min(minLength, right - left + 1)
                sumNums -= nums[left]
                left += 1

        return minLength if minLength <= len(nums) else 0