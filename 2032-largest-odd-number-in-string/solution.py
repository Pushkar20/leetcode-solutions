class Solution:
    def largestOddNumber(self, num: str) -> str:
        for c in range(len(num)- 1, -1, -1):
            if (int(num[c]) % 2) == 1:
                return num[:c+1]
        return ""
