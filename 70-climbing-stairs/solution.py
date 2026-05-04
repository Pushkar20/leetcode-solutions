class Solution:
    def climbStairs(self, n: int) -> int:
        # ways = 0
        # def take_steps(n):
        #     nonlocal ways
        #     if n == 0:
        #         ways += 1
        #         return
        #     else:
        #         if n >= 2:
        #             take_steps(n-2)
        #         take_steps(n-1)
        # take_steps(n)
        # return ways

        if n == 0 or n == 1:
            return 1

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
