# https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i in range(k):
            heap.append((-nums[i], i))

        heapify(heap)

        result = [-heap[0][0]]

        for right in range(k, len(nums)):
            heappush(heap, (-nums[right], right))

            left = right - k
            while heap[0][1] <= left:
                heappop(heap)

            result.append(-heap[0][0])

        return result