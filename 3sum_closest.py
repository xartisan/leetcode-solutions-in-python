class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_distance = 2 ** 32
        nums_len = len(nums)
        rv = None
        for i in range(0, nums_len - 2):
            # opitimization for repeated numbers
            if i > 0 and nums[i] == nums[i - 1] == 0:
                continue
            first, last = i + 1, nums_len - 1
            head_val = nums[i]
            while first < last:
                sum_val = nums[first] + nums[last] + head_val
                cur_distance = abs(target - sum_val)

                if cur_distance < min_distance:
                    min_distance = cur_distance
                    rv = sum_val

                if sum_val == target:
                    return rv
                elif sum_val < target:
                    first += 1
                else:
                    last -= 1
        return rv
                    



