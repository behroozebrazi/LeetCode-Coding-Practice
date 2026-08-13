# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numbers = set(nums)
        maxLength = 0

        for num in numbers:

            if num - 1 not in numbers:
                number = num + 1
                length = 1
                while number in numbers:
                    number += 1
                    length += 1

                maxLength = max(maxLength, length)

        return maxLength