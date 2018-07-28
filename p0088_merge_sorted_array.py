class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        total_len = m + n
        m -= 1
        n -= 1
        for i in range(total_len - 1, -1, -1):
            if n == -1:
                return
            if m == -1 or nums1[m] <= nums2[n]:
                nums1[i] = nums2[n]
                n -= 1
            else:
                nums1[i] = nums1[m]
                m -= 1
