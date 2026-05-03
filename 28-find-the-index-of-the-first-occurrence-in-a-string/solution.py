class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        n = len(needle)
        while index < len(haystack):
            if haystack[index] == needle[0]:
                if haystack[index:n] == needle:
                    return index
                else:
                    index = index + n - 1
            index += 1
        return -1
