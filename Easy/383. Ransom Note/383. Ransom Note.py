# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterR = Counter(ransomNote)
        counterM = Counter(magazine)

        for key, value in counterR.items():
            if key not in counterM or counterM[key] < value:
                return False

        return True