# https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        halfLength = floor(len(nums) / 2)
        counter = Counter(nums)

        for key, value in counter.items():
            if halfLength < value:
                return key


        # majority_candidate = None
        # count = 0

        # for num in nums:
        #     if count == 0:
        #         majority_candidate = num
            
        #     if num == majority_candidate:
        #         count += 1
        #     else:
        #         count -= 1

        # return majority_candidate