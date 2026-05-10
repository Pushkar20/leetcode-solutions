class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        teststr = re.sub(r'[^a-zA-Z0-9]', '', s)
        teststr = teststr.lower()
        if teststr == teststr[::-1]:
            return True
        else:
            return False
