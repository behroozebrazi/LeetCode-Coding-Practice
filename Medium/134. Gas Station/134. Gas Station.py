# https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        totalGas = 0
        remainGas = 0
        startIndex = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            totalGas += diff
            remainGas += diff

            if remainGas < 0:
                remainGas = 0
                startIndex = i + 1

        return startIndex if totalGas >= 0 else -1