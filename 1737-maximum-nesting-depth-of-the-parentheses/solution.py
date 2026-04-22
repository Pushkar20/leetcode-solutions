class Solution:
    def maxDepth(self, s: str) -> int:
        brackets = {")": "(", "]": "[", "}": "{"}
        counter = 0
        max_depth = 0
        for c in s:
            if c in brackets.values():
                counter += 1
            if c in brackets.keys():
                counter -= 1
            if counter > max_depth:
                max_depth = counter
        return max_depth
