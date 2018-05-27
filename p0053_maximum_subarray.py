class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = None
        cur_sum = 0
        start = 0

        for i, num in enumerate(nums):
            if cur_sum <= 0:
                start = i
                cur_sum = 0
            cur_sum += num

            if max_sum is None or cur_sum > max_sum:
                max_sum = cur_sum


        return max_sum
            
