# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows <= 1 or not s:
            return s

        rowIndex = 0
        rowDirection = 0
        lastRowIndex = numRows - 1
        rows = [""] * numRows

        for ch in s:
            rowIndex += rowDirection

            rows[rowIndex] += ch

            if rowIndex == 0:
                rowDirection = 1
            elif rowIndex == lastRowIndex:
                rowDirection = -1

        return "".join(rows)