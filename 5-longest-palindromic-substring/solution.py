class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        l = 0
        r = 0
        n = len(s)
        max_palin = ""

        def run_palin(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1
            return s[l+1:r]

        for i in range(n):
            # print(i, s[i])
            o_palin = run_palin(s, i, i)
            e_palin = run_palin(s, i, i+1)
            if len(o_palin) > len(e_palin):
                palin = o_palin
            else:
                palin = e_palin
            # print(i, palin)
            if len(palin) > len(max_palin):
                max_palin = palin
        return max_palin
