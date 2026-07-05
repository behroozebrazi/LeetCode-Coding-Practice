# https://leetcode.com/problems/shortest-palindrome/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        rest = s[-1]
        s = s[:-1]

        while s != s[::-1]:
            rest += s[-1]
            s = s[:-1]
            
        return rest + s + rest[::-1]