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
            smallest = None
            # for j in range(i + 1, nums_len):
            #     if cur_val < nums[j]:
            #         if smallest is None or nums[j] < nums[smallest]:
            #             smallest = j
            # using binary search
            start, end = i + 1, nums_len - 1
            while start <= end:
                mid = (start + end) // 2
                mid_val = nums[mid]
                if mid_val <= cur_val:
                    start = mid + 1
                else:
                    end = mid - 1
            smallest = start
            if smallest is not None:
                nums[i] = nums[smallest]
                nums[smallest] = cur_val
                done = True
                break
            else:
                # print('xxi', i, nums)
                for k in range(i, nums_len - 1):
                    nums[k] = nums[k + 1]
                nums[-1] = cur_val
                # print(nums)

            i -= 1
        if not done:
            nums.sort()
