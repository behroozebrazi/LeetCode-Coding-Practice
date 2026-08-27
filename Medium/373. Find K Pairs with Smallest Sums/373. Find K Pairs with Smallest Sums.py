# https://leetcode.com/problems/find-k-pairs-with-smallest-sums

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        heap = []
        result = []

        for i in range(min(k, len(nums1))):
            heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and len(result) < k:
            total, i, j = heappop(heap)

            result.append([nums1[i], nums2[j]])

            # Move to the next element in nums2
            j += 1
            if j < len(nums2):
                heappush(heap, (nums1[i] + nums2[j], i, j ))

        return result



# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

#         pairs = []

#         for num1 in nums1:
#             for num2 in nums2:

#                 sumNums = num1 + num2
#                 if len(pairs) == k and sumNums >= -pairs[0][0]:
#                     break

#                 heappush(pairs, (- sumNums, (num1, num2)))
#                 if len(pairs) > k:
#                     heappop(pairs)

#         return [ pair[1] for pair in pairs ]