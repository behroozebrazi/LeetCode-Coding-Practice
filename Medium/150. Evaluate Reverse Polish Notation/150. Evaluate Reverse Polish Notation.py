# https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        result = 0
        stack = []

        for token in tokens:

            match token:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    num = stack.pop()
                    stack.append(stack.pop() - num)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    num = stack.pop()
                    stack.append(int(stack.pop() / num))
                case _:
                    stack.append(int(token))

        return stack.pop()