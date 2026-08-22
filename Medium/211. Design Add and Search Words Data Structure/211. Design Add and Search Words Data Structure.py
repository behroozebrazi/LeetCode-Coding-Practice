# https://leetcode.com/problems/design-add-and-search-words-data-structure

class WordDictionary:

    __base_data_structure = {"exist": False}

    def __init__(self):
        self.data = self.__base_data_structure.copy()


    def addWord(self, word: str) -> None:
        data = self.data
        for ch in word:
            if ch not in data:
                data[ch] = self.__base_data_structure.copy()
            data = data[ch]
        data["exist"] = True


    def search(self, word: str) -> bool:
        return self._dfs(self.data, word)


    def _dfs(self, data, word):
        if not word:
            return data["exist"]
        ch = word[0]

        if ch != ".":
            if ch in data:
                return self._dfs(data[ch], word[1:])
            return False

        for letter in data:
            if letter != "exist" and self._dfs(data[letter], word[1:]):
                return True

        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)