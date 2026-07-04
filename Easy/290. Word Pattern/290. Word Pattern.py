# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        dict1 = dict()
        set1 = set()
        ss = s.split()

        if len(pattern) != len(ss):
            return False

        for i, word in enumerate(ss):
            letter = pattern[i]

            if letter in dict1:
                if dict1[letter] != word:
                    return False
            else:
                if word in set1:
                    return False
                dict1[letter] = word
                set1.add(word)

        return True