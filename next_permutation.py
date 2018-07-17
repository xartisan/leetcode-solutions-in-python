class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        done = False
        for i in range(len(nums) - 2, -1, -1):
            cur_val = nums[i]
            if cur_val >= nums[i + 1]:
                continue
            # insert
            start, end = i + 1, len(nums) - 1

            while start <= end:
                mid = (start + end) // 2
                mid_val = nums[mid]
                if mid_val == cur_val:
                    end = mid - 1
                    while nums[end] == cur_val:
                        end -= 1 
                    break
                elif mid_val < cur_val:
                    end = mid - 1
                else:
                    start = mid + 1
            nums[i], nums[end] = nums[end], nums[i]
            # sort
            start, end = i + 1, len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

            done = True
            break

        if not done:
            nums.sort()
