class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        counter = {}
        for c in t:
            counter[c] = counter.setdefault(c, 0) + 1
        remains = set(t)
        left = -1
        right = len(s)
        cur_left = -1

        for i, c in enumerate(s):
            if c not in counter:
                continue
            if cur_left == -1:
                cur_left = i

            if c in remains:
                counter[c] -= 1
                if counter[c] == 0:
                    remains.remove(c)
            else:
                counter[c] -= 1
                # shrink
                next_cur_left = cur_left
                while True:
                    cc = s[next_cur_left]
                    if cc not in counter:
                        next_cur_left += 1
                        continue
                    if counter[cc] < 0:
                        counter[cc] += 1
                        next_cur_left += 1
                    else:
                        break
                cur_left = next_cur_left
            if not remains and i - cur_left < right - left:
                left, right = cur_left, i
        if left == -1:
            return ""
        return s[left: right + 1]
