# https://leetcode.com/problems/basic-calculator

class Solution:
    def calculate(self, s: str) -> int:

        result = 0
        num = 0
        sign = 1
        stack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            elif c == '+':
                result += sign * num
                num, sign = 0, 1

            elif c == '-':
                result += sign * num
                num, sign = 0, -1

            elif c == '(':
                # Save the current result and sign
                stack.append(result)
                stack.append(sign)

                # Start a new calculation inside parentheses
                result, sign = 0, 1

            elif c == ')':
                # Finish the number inside parentheses
                result += sign * num
                num = 0

                # Restore the previous sign and result
                previous_sign = stack.pop()
                previous_result = stack.pop()

                result = previous_result + previous_sign * result

        # Add the final number
        result += sign * num

        return result