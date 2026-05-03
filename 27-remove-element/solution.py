class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(set(nums)) == 1 and val in set(nums):
            return 0
        lp = 0
        hp = len(nums) - 1
        while lp < hp:
            if nums[lp] == val:
                nums[lp], nums[hp] = nums[hp], nums[lp]
                hp -= 1
            else:
                lp += 1
        return lp+1
