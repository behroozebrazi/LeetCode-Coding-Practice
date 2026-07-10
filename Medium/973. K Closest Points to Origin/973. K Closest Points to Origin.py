# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distances.append((point[0] ** 2 + point[1] ** 2, point))

        heapify(distances)

        result = []
        for i in range(k):
            result.append(heappop(distances)[1])

        return result