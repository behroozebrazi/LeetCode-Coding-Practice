# https://leetcode.com/problems/substring-with-concatenation-of-all-words

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        result = []
        
        if not s or not words:
            return result

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if len(s) < total_len:
            return result

        # Required frequency of each word
        word_freq = Counter(words)

        # Try every possible alignment
        for offset in range(word_len):
            left = offset
            count = 0
            window = {}

            for right in range(offset, len(s) - word_len + 1, word_len):

                word = s[right:right + word_len]

                # Word is not in words
                if word not in word_freq:
                    window.clear()
                    count = 0
                    left = right + word_len
                    continue

                # Add word to current window
                window[word] = window.get(word, 0) + 1
                count += 1

                # Too many copies of this word
                while window[word] > word_freq[word]:
                    left_word = s[left:left + word_len]

                    window[left_word] -= 1
                    left += word_len
                    count -= 1

                # Found all words
                if count == word_count:
                    result.append(left)

                    # Move window forward
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1

        return result


## Second Solution:

# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:

#         result = []
#         word_length = len(words[0])
#         window_length = len(words) * word_length
#         count_words = defaultdict(int)
#         count_letters = defaultdict(int)
#         count_window = defaultdict(int)

#         def wordCounter(st: str) -> {}:
#             word_counter = defaultdict(int)
#             for i in range(0, len(st), word_length):
#                 word_counter[st[i: i + word_length]] += 1
#             return word_counter

#         if not s or not words or len(s) < window_length:
#             return result

#         for w in words:
#             count_words[w] += 1
#             for l in w:
#                 count_letters[l] += 1

#         for i in range(window_length):
#             count_window[s[i]] += 1

#         left = 0
#         right = window_length
#         while right < len(s):
            
#             if count_letters == count_window and count_words == wordCounter(s[left: right]):
#                 result.append(left)

#             count_window[s[right]] += 1
            
#             if count_window[s[left]] > 1:
#                 count_window[s[left]] -= 1
#             else:
#                 del count_window[s[left]]

#             left += 1
#             right += 1

#         if count_letters == count_window and count_words == wordCounter(s[left: right]):
#             result.append(left)

#         return result