class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lp = 0
        hp = len(nums) - 1
        while lp < hp:
            if nums[lp] == val:
                nums[lp], nums[hp] = nums[hp], nums[lp]
                hp -= 1
            else:
                lp += 1
        return lp+1
