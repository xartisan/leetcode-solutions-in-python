class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = -1
        ones = len(nums)

        idx = 0
        while idx < ones:
            num = nums[idx]
            if num <= 1:
                if num == 0:
                    zeros += 1
                    nums[idx], nums[zeros] = nums[zeros], 0
                idx += 1
            else:
                ones -= 1
                nums[idx], nums[ones] = nums[ones], nums[idx]
