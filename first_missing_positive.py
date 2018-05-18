class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        i = 0
        exchange_count = 0
        # O(n) guarantee
        while i < len(nums) and exchange_count < len(nums):
            cur_val = nums[i]
            if cur_val < 0 or cur_val > len(nums) or cur_val == nums[cur_val - 1]:
                i += 1
            else:
                nums[i], nums[cur_val - 1] = nums[cur_val - 1], cur_val
                exchange_count += 1
        for i, v in enumerate(nums, 1):
            if i != v:
                return i
        return len(nums) + 1