class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if len(digits) == 1:
            return list(phone_map[digits])

        else:
            ans = []

            for i in phone_map[digits[0]]:
                for j in self.letterCombinations(digits[1:]):
                    ans.append(i+j)
            return ans
