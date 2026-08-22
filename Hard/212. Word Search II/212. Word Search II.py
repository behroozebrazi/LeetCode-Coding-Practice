# https://leetcode.com/problems/word-search-ii

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        result = []
        m, n = len(board), len(board[0])
        trie = dict()

        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = dict()
                node = node[ch]
            node["word"] = word

        def dfs(row, col, node):
            ch = board[row][col]
            if ch not in node:
                return

            next_node = node[ch]
            if "word" in next_node:
                result.append(next_node["word"])
                del next_node["word"]

            board[row][col] = ""

            if row > 0:
                dfs(row - 1, col, next_node)
            if row + 1 < m:
                dfs(row + 1, col, next_node)
            if col > 0:
                dfs(row, col - 1, next_node)
            if col + 1 < n:
                dfs(row, col + 1, next_node)

            board[row][col] = ch

        for row in range(m):
            for col in range(n):
                dfs(row, col, trie)

        return result