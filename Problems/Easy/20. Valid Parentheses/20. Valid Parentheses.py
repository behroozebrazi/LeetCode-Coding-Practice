# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        queue = []

        for bracket in s:
            if bracket in brackets:
                queue.append(bracket)
            elif queue and brackets[queue[-1]] == bracket:
                queue.pop()
            else:
                return False

        return queue == []