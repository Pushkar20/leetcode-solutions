class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,n = 0,0
        while n < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1
            n += 1
