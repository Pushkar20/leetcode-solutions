class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        while p < len(nums):
            if nums[p] == nums[p-1]:
                nums.pop(p)
                # nums.append(nums[p-1])
            else:
                p += 1
