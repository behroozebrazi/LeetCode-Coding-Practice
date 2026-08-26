# https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_max = max_sum = -30000
        current_min = min_sum = +30000
        total = 0

        for num in nums:
            total += num

            current_max = num if current_max <= 0 else current_max + num
            if max_sum < current_max:
                max_sum = current_max

            current_min = num if current_min >= 0 else current_min + num
            if min_sum > current_min:
                min_sum = current_min

        # All numbers are negative
        if max_sum < 0:
            return max_sum

        circular_max = total - min_sum
        # Either normal or circular
        return max(max_sum, circular_max)