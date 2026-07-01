class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupNums = dict()

        for i, num in enumerate(nums):
            if num in dupNums and i - dupNums[num] <= k:
                return True
            dupNums[num] = i

        return False