class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        n = len(needle)
        while index < len(haystack):
            if haystack[index] == needle[0]:
                # print(n, index, haystack[index:n+index])
                if haystack[index:n+index] == needle:
                    return index
            index += 1
        return -1
