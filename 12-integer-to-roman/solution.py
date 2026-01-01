class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ""
        roman = ""

        rDict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

        i = 1
        while num > 0:
            dig = num % 10
            val = dig*i
            print(f"dig: {dig}, val: {val}, i: {i}")
            if dig != 0:
                if dig != 4 and dig != 9:
                    if val in rDict:
                        s = rDict[val]
                    elif dig > 4:
                        if (val - i) in rDict:
                            s = rDict[val - i] + rDict[val - 5*i]
                        elif (val - 2*i) in rDict:
                            s = rDict[val - (2*i)] + rDict[val - (6*i)] + rDict[val - (6*i)]
                        elif (val - 3*i) in rDict:
                            s = rDict[val - (3*i)] + rDict[val - (7*i)] + rDict[val - (7*i)] + rDict[val - (7*i)]
                    else:
                        if (val - i) in rDict:
                            s = rDict[val - i] + rDict[val - i]
                        elif (val - 2*i) in rDict:
                            s = rDict[val - (2*i)] + rDict[val - (2*i)] + rDict[val - (2*i)]
                elif dig == 4:
                    if val == 4:
                        s = 'IV'
                    else:
                        s = rDict[val - (3*i)] + rDict[val + i]
                else:
                    if val == 9:
                        s = 'IX'
                    else:
                        s = rDict[val - (8*i)] + rDict[val + i]
                
                roman = s + roman
            num = num // 10
            i = i*10
        return roman
