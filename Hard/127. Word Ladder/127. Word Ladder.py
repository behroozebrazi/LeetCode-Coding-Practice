# https://leetcode.com/problems/word-ladder

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        letters = "abcdefghijklmnopqrstuvwxyz"
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            lastWord, changes = queue.popleft()

            for i, ch in enumerate(lastWord):
                for letter in letters:

                    if ch == letter:
                        continue

                    newWord = lastWord[:i] + letter + lastWord[i + 1:]

                    if newWord == endWord:
                        return changes + 1

                    if newWord in words:
                        queue.append((newWord, changes + 1))
                        words.remove(newWord)

        return 0



# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

#         letters = "abcdefghijklmnopqrstuvwxyz"
#         words = set(wordList)

#         if endWord not in words:
#             return 0

#         queue = deque([(beginWord, 1)])
#         visited = set([beginWord])

#         while queue:
#             lastWord, changes = queue.popleft()

#             for i, ch in enumerate(lastWord):
#                 for letter in letters:

#                     if ch == letter:
#                         continue

#                     newWord = lastWord[:i] + letter + lastWord[i + 1:]

#                     if newWord == endWord:
#                         return changes + 1

#                     if newWord in words and newWord not in visited:
#                         queue.append((newWord, changes + 1))
#                         visited.add(newWord)

#         return 0