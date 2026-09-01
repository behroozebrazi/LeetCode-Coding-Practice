# https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)
        word_lengths = {len(word) for word in words}

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for j in range(1, len(dp)):
            for length in word_lengths:
                i = j - length

                if i >= 0 and dp[i] and s[i:j] in words:
                    dp[j] = True
                    break

        return dp[-1]



# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:

#         words = set(wordDict)
#         dp = [False] * (len(s) + 1)
#         dp[0] = True

#         for j in range(1, len(dp)):
#             for i in range(j):
#                 if dp[i] and s[i:j] in words:
#                     dp[j] = True
#                     break

#         return dp[-1]