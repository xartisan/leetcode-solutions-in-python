class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        fac = math.factorial(n - 1)
        rv = []
        nums = list(range(1, n + 1))

        k -= 1
        while k != 0:
            idx = k // fac
            rv.append(nums[idx])
            nums = nums[:idx] + nums[idx + 1:]
            k %= fac
            fac //= (n - 1) 
            n -= 1

        rv.extend(nums)
        return ''.join(str(x) for x in rv)