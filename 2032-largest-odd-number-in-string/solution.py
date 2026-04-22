class Solution:
    def largestOddNumber(self, num: str) -> str:
        LON = float("-inf")
        for c in range(len(num)):
            if (int(num[c]) % 2) != 0:
                LON = num[0:c+1]
        if LON == float("-inf"):
            return ""
        else:
            return str(LON)
