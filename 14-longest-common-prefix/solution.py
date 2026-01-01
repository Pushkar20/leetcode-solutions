class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        n = len(strs)
        try:
            i = 0
            while 1:
                str_set = set()
                for item in strs:
                    str_set.add(item[i])
                if len(str_set) == 1:
                    s = s + item[i]
                else:
                    break
                i += 1
        except:
            return s
        return s
