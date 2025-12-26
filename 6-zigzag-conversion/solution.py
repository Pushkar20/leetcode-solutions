class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        rf = False
        final = ""
        hm = {}
        for i in range(numRows):
            hm[i+1] = ""
        i = 1
        for c in s:
            # print(i, c)
            if not rf:
                hm[i] = hm[i] + c
                if i % numRows == 0:
                    rf = not rf
                    i = i - 1
                    continue
                i = i + 1
            else:
                hm[i] = hm[i] + c
                if i % numRows == 1:
                    rf = not rf
                    i = i + 1
                    continue
                i = i - 1
            # print(hm)
        for i in range(numRows):
            final = final + hm[i+1]
        return final
