# https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, current):
            # Base case
            if index == len(digits):
                result.append("".join(current))
                return

            # Try every letter for this digit
            for letter in phone[digits[index]]:
                current.append(letter)

                backtrack(index + 1, current)

                # Undo the choice
                current.pop()

        backtrack(0, [])

        return result



# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:

#         result = []
#         digit = list(digits)
#         char = list('abcdefghijklmnopqrstuvwxyz')
#         numbers = {
#             '2': char[0:3], 
#             '3': char[3:6],
#             '4': char[6:9],
#             '5': char[9:12],
#             '6': char[12:15],
#             '7': char[15:19],
#             '8': char[19: 22],
#             '9': char[22:]
#         }

#         while digit:
#             letters = numbers[digit[0]]
#             digit = digit[1:]
#             i = 0

#             if len(result) > 0:
#                 size = len(result)
#                 result = result * len(letters)
#                 for ch in letters:
#                     for _ in range(size):
#                         result[i] += ch
#                         i += 1
#             else:
#                 result = letters

#         return result