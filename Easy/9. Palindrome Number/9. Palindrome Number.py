# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reverse_half = 0

        while x > reverse_half:
            x, mod = divmod(x, 10)
            reverse_half = reverse_half * 10 + mod

        return x == reverse_half or x == reverse_half // 10



# class Solution:
#     def isPalindrome(self, x: int) -> bool:
        
#         sf = str(x)
#         sr = sf[::-1]
#         half =  floor(len(sf) / 2)

#         return sf[ : half] == sr[ : half]