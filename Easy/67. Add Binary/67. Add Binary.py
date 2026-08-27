# https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # (carry, digit 1, digit 2)
        digit = {
            ('0', '0', '0'): ('0', '0'),
            ('0', '0', '1'): ('0', '1'),
            ('0', '1', '0'): ('0', '1'),
            ('0', '1', '1'): ('1', '0'),
            ('1', '0', '0'): ('0', '1'),
            ('1', '0', '1'): ('1', '0'),
            ('1', '1', '0'): ('1', '0'),
            ('1', '1', '1'): ('1', '1'),
            }
        total = ""
        carry = '0'
        na = len(a)
        nb = len(b)

        while na > 0 or nb > 0 or carry == '1':
            na -= 1
            nb -= 1
            aNum = a[na] if na >= 0 else '0'
            bNum = b[nb] if nb >= 0 else '0'

            carry, sumNum = digit[(carry, aNum, bNum)]
            total = sumNum + total

        return total



# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         i = len(a)
#         j = len(b)
#         carry = 0
#         result = ''

#         while i > 0 or j > 0 or carry:
#             total = carry

#             if i > 0:
#                 i -= 1
#                 total += int(a[i])

#             if j > 0:
#                 j -= 1
#                 total += int(b[j])

#             carry, remain = divmod(total, 2)
#             result = str(remain) + result

#         return result



# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a, 2) + int(b, 2))[2:]