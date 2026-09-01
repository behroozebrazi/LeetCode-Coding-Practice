# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s

        longest = ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            # Odd-length palindrome
            palindrome1 = expand(i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1

            # Even-length palindrome
            palindrome2 = expand(i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest