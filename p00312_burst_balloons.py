class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        full_nums = [1] 
        full_nums.extend(nums)
        full_nums.append(1)

        record = [[-1] * len(full_nums) for _ in range(len(full_nums))]

        for i in range(1, len(full_nums)):
            for j in range(i, len(full_nums)):
                record[i][j] = -1
        

        def _max_coins(start, end):
            if start > end:
                return 0
            if record[start][end] != -1:
                return record[start][end]     
            
            for pos in range(start, end + 1):
                left_coins = _max_coins(start, pos - 1)
                pos_coins = full_nums[start - 1] * full_nums[pos] * full_nums[end + 1]
                right_coins = _max_coins(pos + 1, end)
                max_coins = left_coins + pos_coins + right_coins
                if max_coins > record[start][end]:
                    record[start][end] = max_coins
            return record[start][end]

        return _max_coins(1, len(full_nums) - 2)