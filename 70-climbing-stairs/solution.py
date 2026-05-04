class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0

        def take_steps(n):
            nonlocal ways
            if n == 0:
                ways += 1
                return
            else:
                if n >= 2:
                    take_steps(n-2)
                take_steps(n-1)

        take_steps(n)
        return ways
