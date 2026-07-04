# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        halfLength = floor(len(nums) / 2)
        count = Counter(nums)
        
        for key, value in count.items():
            if halfLength < value:
                return key