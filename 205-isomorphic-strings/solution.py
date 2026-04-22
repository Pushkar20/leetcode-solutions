class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mem = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in mem.keys():
                if t[i] != mem[s[i]]:
                    return False
            else:
                mem[s[i]] = t[i]
        return True
