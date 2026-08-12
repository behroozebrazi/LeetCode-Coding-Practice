# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        noRepeatNum = set()
        pattern = dict()

        for index, sLetter in enumerate(s):
            tLetter = t[index]

            if sLetter in pattern:
                if tLetter != pattern[sLetter]:
                    return False

            else:
                if tLetter in noRepeatNum:
                    return False
                noRepeatNum.add(tLetter)
                pattern[sLetter] = tLetter

        return True