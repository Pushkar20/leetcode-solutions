class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) - 1
        i = 0

        def expand_mid(nums, mid):
            l = r = mid
            while l > 0 and nums[l] == nums[l-1]:
                l -= 1
            while r < (len(nums)-1) and nums[r] == nums[r+1]:
                r += 1
            return [l, r]

        while i <= n:
            mid = (i + n) // 2
            if nums[mid] == target:
                return expand_mid(nums, mid)
            elif nums[mid] < target:
                i = mid + 1
            else:
                n = mid - 1
        return [-1, -1]
