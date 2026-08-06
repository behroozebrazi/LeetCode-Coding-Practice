# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for letter in s[::-1]:

            if letter != ' ':
                length += 1

            else:
                if length > 0:
                    return length

        return length