class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffNums = dict()

        for i, num in enumerate(nums):
            if num in diffNums:
                return [diffNums[num], i]
            diffNums[target - num] = i