# https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if self.stack and self.stack[-1][1] < value:
            self.stack.append((value, self.stack[-1][1]))
        else:
            self.stack.append((value, value))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]