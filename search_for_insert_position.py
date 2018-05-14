class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            mid_val = nums[mid]

            if target == mid_val:
                return mid
            elif target < mid_val:
                end = mid - 1
            else:
                start = mid + 1
            
        return start