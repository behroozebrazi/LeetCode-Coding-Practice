# https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        pointerS = 0
        lengthS = len(s)

        if lengthS == 0:
            return True

        for ch in t:
            if ch == s[pointerS]:
                pointerS += 1
                if pointerS >= lengthS:
                    return True

        return False