# https://leetcode.com/problems/h-index

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        if len(citations) == 1 and citations[0] > 0:
            return 1

        citations.sort(reverse=True)

        for i, citation in enumerate(citations):
            if i >= citation:
                return i

        return len(citations)