# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:

        counter = Counter(s)

        for index, ch in enumerate(s):
            if counter[ch] == 1:
                return index

        return -1