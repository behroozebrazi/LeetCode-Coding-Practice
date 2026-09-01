# https://leetcode.com/problems/max-points-on-a-line

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        result = 0
        for i in range(n):
            slopes = defaultdict(int)

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0:
                    dy = 1
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                slope = (dy, dx)
                count = slopes[slope] + 1
                slopes[slope] = count
                if result < count:
                    result = count

        return result + 1