# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

        def find_first():
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    result[0] = mid
                    right = mid - 1

        def find_last():
            if result[0] < 0: return

            left = result[0]
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    result[1] = mid
                    left = mid + 1

        find_first()
        find_last()
        return result