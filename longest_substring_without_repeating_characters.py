class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # cur_longest = ''
        max_len = 0
        start = 0
        record = {}

        for i, c in enumerate(s, 1):
            last_c_index = record.get(c)
            if last_c_index is None or last_c_index < start:
                cur_len = i - start
                max_len = max(cur_len, max_len)
            else:
                start = last_c_index + 1
            record[c] = i - 1
        return max_len


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3, 'Wrong Answer!'
    assert s.lengthOfLongestSubstring("bbbbb") == 1, 'Wrong Answer!'
    assert s.lengthOfLongestSubstring("pwwkew") == 3, 'Wrong Answer!'
