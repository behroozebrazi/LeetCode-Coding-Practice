# https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []


    def addNum(self, num: int) -> None:
        if self.left and num < -self.left[0]:
            heappush(self.left, -num)
        else:
            heappush(self.right, num)

        diff =  len(self.right) - len(self.left)
        if diff < 0:
            heappush(self.right, - heappop(self.left))
        elif diff > 1:
            heappush(self.left, - heappop(self.right))


    def findMedian(self) -> float:
        if len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (self.right[0] - self.left[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



# class MedianFinder:

#     def __init__(self):
#         self.left = []
#         self.right = []


#     def addNum(self, num: int) -> None:
#         heappush(self.right, num)

#         if self.left and -self.left[0] > self.right[0]:
#             heappush(self.right, - heappop(self.left))

#         while len(self.right) - len(self.left) > 1:
#             heappush(self.left, - heappop(self.right))


#     def findMedian(self) -> float:
        
#         if len(self.right) == 0:
#             return 0
        
#         if len(self.left) < len(self.right):
#             return self.right[0]
#         else:
#             return (self.right[0] - self.left[0]) / 2



# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()