# https://leetcode.com/problems/substring-with-concatenation-of-all-words

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        result = []
        word_length = len(words[0])
        window_length = len(words) * word_length
        count_words = defaultdict(int)
        count_letters = defaultdict(int)
        count_window = defaultdict(int)

        def wordCounter(st: str) -> {}:
            word_counter = defaultdict(int)
            for i in range(0, len(st), word_length):
                word_counter[st[i: i + word_length]] += 1
            return word_counter

        if not s or not words or len(s) < window_length:
            return result

        for w in words:
            count_words[w] += 1
            for l in w:
                count_letters[l] += 1

        for i in range(window_length):
            count_window[s[i]] += 1

        left = 0
        right = window_length
        while right < len(s):
            
            if count_letters == count_window and count_words == wordCounter(s[left: right]):
                result.append(left)

            count_window[s[right]] += 1
            
            if count_window[s[left]] > 1:
                count_window[s[left]] -= 1
            else:
                del count_window[s[left]]

            left += 1
            right += 1

        if count_letters == count_window and count_words == wordCounter(s[left: right]):
            result.append(left)

        return result