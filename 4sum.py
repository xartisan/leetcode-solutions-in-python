class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        rv = []
        nums_len = len(nums)
        # one more level of loop than 3sum problem
        for i in range(0, nums_len - 3):
            # optimization for specific situations
            if target < nums[i] * 4 or target > nums[-1] * 4:
                return rv
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, nums_len - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
        
                new_target = target - nums[i] - nums[j]
                first, last = j + 1, nums_len - 1
                while first < last:
                    sum_val = nums[first] + nums[last]
                    if sum_val == new_target:
                        rv.append([nums[i], nums[j], nums[first], nums[last]])
                        while first < last and nums[first] == nums[first + 1]:
                            first += 1
                        while last > first and nums[last] == nums[last - 1]:
                            last -= 1
                        first, last = first + 1, last - 1
                    elif sum_val < new_target:
                        first += 1
                    else:
                        last -= 1

        return rv