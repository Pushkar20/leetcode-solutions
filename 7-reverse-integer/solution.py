class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        ans = ""
        for i in reversed(y):
            if i == '-':
                continue
            ans = ans + i
        if x < 0:
            ans = '-' + ans
        ans = int(ans)
        if ans < -2**31 or ans > (2**31 - 1):
            ans = 0
        return ans
