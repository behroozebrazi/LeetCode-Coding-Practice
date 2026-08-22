# https://leetcode.com/problems/implement-trie-prefix-tree

class Trie:

    __base_data_structure = {"exist": False}

    def __init__(self):
        self.data = self.__base_data_structure.copy()


    def insert(self, word: str) -> None:
        data = self.data
        for ch in word:
            if ch not in data:
                data[ch] = self.__base_data_structure.copy()
            data = data[ch]
        data["exist"] = True


    def search(self, word: str) -> bool:
        data = self.data
        for ch in word:
            if ch not in data:
                return False
            data = data[ch]
        return data["exist"]


    def startsWith(self, prefix: str) -> bool:
        data = self.data
        for ch in prefix:
            if ch not in data:
                return False
            data = data[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



# class Trie:

#     __base_data_structure = {"word": ""}
#     for letter in "abcdefghijklmnopqrstuvwxyz":
#         __base_data_structure[letter] = None

#     def __init__(self):
#         self.data = self.__base_data_structure.copy()


#     def insert(self, word: str) -> None:
#         data = self.data
#         for ch in word:
#             if not data[ch]:
#                 data[ch] = self.__base_data_structure.copy()
#             data = data[ch]
#         data["word"] = word


#     def search(self, word: str) -> bool:
#         data = self.data
#         for ch in word:
#             if not data[ch]:
#                 return False
#             data = data[ch]
#         return data["word"] == word


#     def startsWith(self, prefix: str) -> bool:
#         data = self.data
#         for ch in prefix:
#             if not data[ch]:
#                 return False
#             data = data[ch]
#         return True


# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)