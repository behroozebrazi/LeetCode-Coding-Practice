# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        compareLength = len(needle)
        firstChar = needle[0]

        for i in range(n - compareLength + 1):

            if haystack[i] == firstChar and needle == haystack[i: min(n, i + compareLength)]:
                return i

        return -1