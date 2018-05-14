class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            start_val, end_val = nums[start], nums[end]
            if start_val <= end_val and (target < start_val or target > end_val):
                return -1
            
            mid = (start + end) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            elif target < mid_val:
                if start_val <= mid_val and target < start_val:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if mid_val <= end_val and target > end_val:
                    end = mid - 1
                else:
                    start = mid + 1

        return -1
        