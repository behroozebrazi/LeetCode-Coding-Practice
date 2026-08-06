# https://leetcode.com/problems/insert-delete-getrandom-o1

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.valIdx = dict()


    def insert(self, val: int) -> bool:
        if val not in self.valIdx:
            self.valIdx[val] = len(self.values)
            self.values.append(val)
            return True
        return False


    def remove(self, val: int) -> bool:
        if val in self.valIdx:
            removeIdx = self.valIdx[val]
            replaceVal = self.values[-1]
            self.valIdx[replaceVal] = removeIdx
            self.values[removeIdx] = replaceVal
            del self.valIdx[val]
            self.values.pop()
            return True
        return False


    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()