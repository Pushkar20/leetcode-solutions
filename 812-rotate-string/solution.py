class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i] == goal[0]:
                trial = s[i:] + s[:i]
                if trial == goal:
                    return True
        return False
