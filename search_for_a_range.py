class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            mid_val = nums[mid]
            if target == mid_val:
                i = mid
                while nums[start] != mid_val:
                    m = (start + i) // 2
                    m_val = nums[m]
                    if m_val == mid_val:
                        i = m
                    else:
                        start = m + 1
                i = mid
                while nums[end] != mid_val:
                    m = (i + end + 1) // 2
                    m_val = nums[m]

                    if m_val == mid_val:
                        i = m
                    else:
                        end = m - 1
                return [start, end]
            elif target > mid_val:
                start = mid + 1
            else:
                end = mid - 1
        return [-1, -1]