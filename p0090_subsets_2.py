class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()

        rv = [[]]
        last_add_num = 0
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                for j in range(len(rv) - last_add_num, len(rv)):
                    rv.append(rv[j] + [num])
            else:
                last_add_num = len(rv)
                rv += [item + [num] for item in rv]
        return rv