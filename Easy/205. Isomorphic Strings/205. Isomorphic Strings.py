# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        noRepeatNum = set()
        pattern = dict()

        for index, ch in enumerate(s):
            if ch in pattern:
                if t[index] != pattern[ch]:
                    return False
            else:
                if t[index] in noRepeatNum:
                    return False
                noRepeatNum.add(t[index])
                pattern[ch] = t[index]

        return True