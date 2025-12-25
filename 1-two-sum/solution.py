class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        if len(nums) == 2:
            return [0,1]
        for i, n in enumerate(nums):
            # print(i)
            # print(hm)
            if n not in hm:
                hm[target - n] = i
            else:
                return [hm[n],i]
