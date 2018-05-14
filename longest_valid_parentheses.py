class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        # ())()
        # record for )
        # record[1] = 0
        # record.get(2) is None
        record = {}

        for i, p in enumerate(s):
            if p == ')':
                if i - 1 < 0:
                    continue
                flag = False
                if s[i - 1] == ')':
                    lpos = record.get(i - 1)
                    if lpos is not None and lpos - 1 >= 0 and s[lpos - 1] == '(':
                        record[i] = lpos - 1
                        flag = True
                        if lpos - 2 >= 0 and record.get(lpos - 2) is not None:
                            record[i] = record[lpos - 2]
                else:
                    flag = True
                    record[i] = i - 1
                    # print('else-> record', record)
                    # print('get', record.get(i - 2))
                    if i - 2 >= 0 and record.get(i - 2) is not None:
                        record[i] = record[i - 2]
                # update max_len 
                if flag:
                    cur_len = i - record[i] + 1
                    if cur_len > max_len:
                        max_len = cur_len
        return max_len
