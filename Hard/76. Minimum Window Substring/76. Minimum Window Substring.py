# https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        need = defaultdict(int)
        window = defaultdict(int)

        for char in t:
            need[char] += 1

        left = 0
        right = 0

        formed = 0
        required = len(need)

        min_length = float("inf")
        min_left = 0

        while right < len(s):
            char = s[right]

            window[char] += 1

            # This character now satisfies its required count
            if char in need and window[char] == need[char]:
                formed += 1

            # Window is valid → try to make it smaller
            while formed == required:
                # Save the smallest window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left

                left_char = s[left]
                window[left_char] -= 1

                # Window is no longer valid
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

            right += 1

        if min_length == float("inf"):
            return ""

        return s[min_left:min_left + min_length]


## Second Solution

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:

#         def isSubstring(count1: dict, count2: dict) -> bool:
#             for key, val in count1.items():
#                 if key not in count2 or count2[key] < val:
#                     return False
#             return True

#         result = ""
#         minLength = len(s) + 1

#         if len(s) < len(t):
#             return result

#         count_t = Counter(t)
#         window = defaultdict(int)
#         for i in range(len(t) - 1):
#             window[s[i]] += 1

#         left = 0
#         right = len(t) - 1
        
#         while right < len(s):
#             window[s[right]] += 1
#             right += 1

#             if isSubstring(count_t, window):
#                 while isSubstring(count_t, window):
#                     window[s[left]] -= 1
#                     left += 1
#                 if  right - left < minLength :
#                     result = s[left - 1: right]
#                     minLength = right - left

#         return result