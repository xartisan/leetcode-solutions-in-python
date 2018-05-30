class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        rv = []

        def helper(acc, start, end, lefts):
            if lefts == 0:
                rv.append(acc)
                return
            # if start > end:
            #     return
            to_choose_num = end - start + 1
            if to_choose_num == lefts:
                rv.append(acc + list(range(start, end + 1)))
                return
            elif to_choose_num < lefts:
                return

            helper(acc + [start], start + 1, end, lefts -1)
            helper(acc, start + 1, end, lefts)
        helper([], 1, n, k)
        return rv