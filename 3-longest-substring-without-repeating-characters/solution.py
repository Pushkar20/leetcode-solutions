class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        p1 = 0
        ss = ""
        max_len = 0
        for p2 in range(n):
            if s[p2] not in ss:
                ss = ss + s[p2]
                # print('if ',ss)
            else:
                while s[p2] in ss:
                    p1 = p1 + 1
                    ss = s[p1:p2]
                    # print('inwhile ', ss)
                ss = ss + s[p2]
                # print('else',ss)
            if max_len < len(ss):
                max_len = len(ss)
            # print(max_len)
        return max_len
