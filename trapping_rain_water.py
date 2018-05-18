class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        cur_water = 0
        stack = []
        for i, n in enumerate(height):
            if n == 0:
                continue
            last_h =0
            while stack and stack[-1][1] <= n:
                cur_i, cur_h = stack.pop()
                cur_water += (cur_h - last_h) * (i - cur_i - 1)
                last_h = cur_h
            #
            if stack and n > last_h:
                cur_water += (n - last_h) * (i - stack[-1][0] - 1)
            stack.append((i, n))
        return cur_water