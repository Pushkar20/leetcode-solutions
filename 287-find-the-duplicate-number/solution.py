class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mem = {}

        for i in nums:
            if i in mem:
                return i
            else:
                mem[i] = 0
        return None
