# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        directory = path.split('/')

        for name in directory:
            if not name or name == '.':
                continue

            if name == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(name)

        return '/' + '/'.join(stack)