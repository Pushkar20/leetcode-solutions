class Solution:
    def myAtoi(self, s: str) -> int:
        my_str = ""
        sign = ""
        for i in s:
            if i == " " and sign == "" and my_str == "":
                continue
            if i == "-" and sign == "" and my_str == "":
                sign = "-"
                continue
            if i == "+" and sign == "" and my_str == "":
                sign = "+"
                continue
            try:
                if int(i) in range(0,10):
                    my_str = my_str + i
            except:
                break
        if my_str == "":
            return 0
        ans = int(sign + my_str)
        if ans < -2**31:
            ans = -2**31
        elif ans > (2**31 - 1):
            ans = (2**31 - 1)
        return ans
