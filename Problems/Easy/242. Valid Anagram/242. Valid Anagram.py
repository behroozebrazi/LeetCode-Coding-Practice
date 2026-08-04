# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counterS = defaultdict(int)
        counterT = defaultdict(int)

        for i, ch in enumerate(s):
            counterS[ch] += 1
            counterT[t[i]] += 1

        return counterS == counterT