# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        maxLengthSubstring = 0
        substringLetter = set()

        for right, ch in enumerate(s):

            while ch in substringLetter:
                substringLetter.remove(s[left])
                left += 1

            substringLetter.add(ch)
            maxLengthSubstring = max(maxLengthSubstring, right - left + 1)

        return maxLengthSubstring