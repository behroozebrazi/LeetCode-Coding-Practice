# https://leetcode.com/problems/summary-ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        result = []

        if len(nums) < 1:
            return result

        first = last = nums[0]

        for num in nums:

            if num - last > 1:
                res = str(first) + ("->" + str(last) if first != last else "")
                result.append(res)
                first = num

            last = num

        res = str(first) + ("->" + str(last) if first != last else "")
        result.append(res)

        return result