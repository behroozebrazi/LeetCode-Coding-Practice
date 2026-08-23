# https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        nn = n * 2

        def backtrack(path, open, close):
            if len(path) == nn:
                result.append("".join(path))
                return

            # We can add '(' if we haven't used all of them
            if open < n:
                path.append("(")
                backtrack(path, open + 1, close)
                path.pop()

            # We can add ')' only if there is an unmatched '('
            if close < open:
                path.append(")")
                backtrack(path, open, close + 1)
                path.pop()

        backtrack([], 0, 0)

        return result