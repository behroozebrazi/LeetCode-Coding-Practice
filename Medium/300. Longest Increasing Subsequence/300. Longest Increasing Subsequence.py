# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        longest = 0
        dp = [1] * len(nums)

        for i in range(len(nums)):
            local_max = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    local_max = max(local_max, dp[j] + 1)
            dp[i] = local_max
            longest = max(longest, local_max)

        return longest



# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:

#         tail = []

#         for num in nums:
#             idx = bisect_left(tail, num)
#             if idx == len(tail):
#                 tail.append(num)
#             else:
#                 tail[idx] = num

#         return len(tail)