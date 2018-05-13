class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        words_counter = {}
        for word in words:
            words_counter[word] = words_counter.setdefault(word, 0) + 1
        num_words = len(words)
        word_len = len(words[0])
        total_len = num_words * word_len
        rv = []

        for i in range(len(s) - total_len + 1):
            record = {}
            match = True
            for j in range(i, i + total_len, word_len):
                w = s[j: j + word_len]
                if w not in words_counter:
                    match = False
                    break
                record[w] = record.setdefault(w, 0) + 1
                if record[w] > words_counter[w]:
                    match = False
                    break
            if match:
                rv.append(i)
        
        return rv
