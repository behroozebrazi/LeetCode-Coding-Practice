# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        first = strs[0]
        last = strs[-1]
        minLength = min(len(first), len(last))
        result = ""

        for i in range(minLength):
            if (first[i] != last[i]):
                return result
            result += first[i]

        return result