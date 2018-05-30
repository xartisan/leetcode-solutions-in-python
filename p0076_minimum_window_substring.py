class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        counter = Counter(t)
        min_start = min_end = -1
        remains = len(t)
        more_chars = {}
        cur_start = cur_end = -1

        for i, c in enumerate(s):
            v = counter.get(c)
            if v is None:
                continue
            # c in target
            # update start end
            cur_end = i
            if cur_start == -1:
                cur_start = i

            if v != 0:
                counter[c] -= 1
                remains -= 1
                if remains == 0:
                    min_start = cur_start
                    min_end = i
            else:
                more_chars[c] = more_chars.setdefault(c, 0) + 1

                if s[cur_start] == c:
                    for l in range(cur_start, i + 1):
                        char = s[l]
                        if char not in counter:
                            continue
                        count = more_chars.get(char)
                        if count is None or count == 0:
                            break
                        more_chars[char] -= 1

                    cur_start = l
                    if remains == 0 and cur_end - cur_start < min_end - min_start:
                        min_start = cur_start
                        min_end = cur_end
            
        return s[min_start:min_end + 1]
