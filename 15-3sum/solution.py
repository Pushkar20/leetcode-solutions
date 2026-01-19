class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if (nums[0] + nums[1] + nums[2]) == 0:
                return [nums]
            else:
                return []

        def two_sum(target, nums):
            hm = {}
            if len(nums) == 2:
                return [0,1]
            for i, n in enumerate(nums):
                if n not in hm:
                    hm[target - n] = i
                else:
                    # return [hm[n],i]
                    return [nums[hm[n]],nums[i]]
            # print(target, nums, hm)

        final_set = set()
        mem_2d = {}
        for i, n in enumerate(nums):
            if n not in mem_2d:
                mem_2d[n] = two_sum(0-n, nums)
        # print(mem_2d)
        for key, item in mem_2d.items():
            if item:
                arr = [key] + item
                arr.sort()
                coords = tuple(arr)
                final_set.add(coords)
        return list(final_set)
