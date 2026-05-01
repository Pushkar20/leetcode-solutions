class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        mem = []
        counter = 0
        for c in s:
            if c == ')':
                if mem:
                    mem.pop()
                else:
                    counter += 1
            else:
                mem.append(c)
        counter += len(mem)
        return counter
