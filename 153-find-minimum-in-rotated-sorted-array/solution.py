class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= nums[r]:
                if nums[mid] <= nums[l]:
                    return nums[mid]
                r = mid - 1
            else:
                if nums[mid] <= nums[r]:
                    return nums[mid]
                l = mid + 1
        return -1
