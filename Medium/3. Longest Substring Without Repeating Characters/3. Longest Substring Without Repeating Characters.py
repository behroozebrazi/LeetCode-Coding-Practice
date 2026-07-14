# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        j = 0
        maxLength = 0

        for i, ch in enumerate(s):

            while ch in charSet:
                charSet.remove(s[j])
                j += 1

            charSet.add(ch)
            maxLength = max(maxLength, i - j + 1)

        return maxLength