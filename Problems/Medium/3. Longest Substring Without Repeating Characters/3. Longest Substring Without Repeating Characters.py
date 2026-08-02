# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substringChar = set()

        j = 0
        maxLengthSubstring = 0

        for i, ch in enumerate(s):

            while ch in substringChar:
                substringChar.remove(s[j])
                j += 1

            substringChar.add(ch)
            maxLengthSubstring = max(maxLengthSubstring, i - j + 1)

        return maxLengthSubstring