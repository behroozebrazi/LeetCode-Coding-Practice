# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        singleNums = set()

        for num in nums:
            if num in singleNums:
                return True
            singleNums.add(num)
            
        return False