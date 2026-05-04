class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        import re
        ls = re.findall(r"\b\w+\b", s)
        return len(ls[-1])
