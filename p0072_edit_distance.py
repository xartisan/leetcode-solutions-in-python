class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dynamic programming methods
        len1 = len(word1)
        len2 = len(word2)

        record = [[0] * (len1 + 1) for _ in range(len2 + 1)]

        for i in range(0, len1 + 1):
            record[0][i] = i
        for i in range(0, len2 + 1):
            record[i][0] = i

        for i2 in range(1, len2 + 1):
            for i1 in range(1, len1 + 1):
                cost = 0 if word1[i1 - 1] == word2[i2 - 1] else 1
                record[i2][i1] = min(record[i2 - 1][i1] + 1,
                record[i2][i1 - 1] + 1, record[i2 - 1][i1 - 1] + cost)
        return record[len2][len1]
