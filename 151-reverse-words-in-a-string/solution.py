class Solution:
    def reverseWords(self, s: str) -> str:
        import re
        lst = re.findall(r"\b(\w+)\b", s)
        lst = lst[::-1]
        ans = " ".join(lst)
        return ans
