class Solution:
    def romanToInt(self, s: str) -> int:
        rDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s[::-1]
        val = 0
        i = 0
        while i < len(s):
            # print(f"i: {i}, {s[i]}")
            val = val + rDict[s[i]]
            if i+1 < len(s):
                if rDict[s[i]] > rDict[s[i+1]]:
                    val = val - rDict[s[i+1]]
                    i += 1
            i += 1
            # print(val)
        return val
