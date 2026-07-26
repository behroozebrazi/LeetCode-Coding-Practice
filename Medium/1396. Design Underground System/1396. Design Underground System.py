# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.traveled = dict()
        self.travel = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travel[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        destination, startTime = self.travel.pop(id)
        key = (destination, stationName)
        lst = self.traveled[key] if key in self.traveled else [0, 0]
        self.traveled[key] = [lst[0] + t - startTime, lst[1] + 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        lst = self.traveled[(startStation, endStation)]
        return lst[0] / lst[1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)