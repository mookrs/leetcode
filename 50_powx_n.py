class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def power(x, n):
            if n == 0:
                return 1
            v = self.myPow(x, n // 2)
            if n % 2 == 0:
                return v * v
            else:
                return v * v * x

        if n < 0:
            return 1 / power(x, -n)
        else:
            return power(x, n)


s = Solution()
print(s.myPow(2.00000, 10))
print(s.myPow(2.10000, 3))
print(s.myPow(2.00000, -2))
