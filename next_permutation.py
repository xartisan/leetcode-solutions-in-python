class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        # 2 3 4 3
        i = nums_len - 2
        done = False
        while i >= 0:
            cur_val = nums[i]
            # using binary search
            start, end = i + 1, nums_len - 1
            while start <= end:
                mid = (start + end) // 2
                mid_val = nums[mid]
                if mid_val <= cur_val:
                    start = mid + 1
                else:
                    end = mid - 1
            if start < nums_len:
                nums[i] = nums[start]
                nums[start] = cur_val
                done = True
                break
            else:
                for k in range(i, nums_len - 1):
                    nums[k] = nums[k + 1]
                nums[-1] = cur_val

            i -= 1
        if not done:
            nums.sort()
