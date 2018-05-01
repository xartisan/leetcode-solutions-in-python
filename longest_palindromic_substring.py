class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dim = len(s)
        longest = ''
        max_len = 0
        record = [[False] * dim for i in range(dim)]

        for i in range(dim):
            j = i
            while j >= 0:
                if s[j] == s[i] and (i - j < 2 or record[j + 1][i - 1]):
                    record[j][i] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        longest = s[j:i + 1]
                j -= 1

        return longest


if __name__ == '__main__':
    s = Solution()
    assert s.longestPalindrome('babad') == 'bab', 'Wrong Answer!'
    assert s.longestPalindrome('cbbd', 'bb')
