# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        result = []
        count = Counter(nums)

        for key, value in count.items():
            heap.append((-value, key))

        heapq.heapify(heap)

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result