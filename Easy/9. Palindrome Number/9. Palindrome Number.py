# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        sf = str(x)
        sr = sf[::-1]
        half =  floor(len(sf) / 2)

        return sf[ : half] == sr[ : half]