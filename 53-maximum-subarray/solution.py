class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        max_ = 0
        if len(nums) == 1:
            return nums[0]
        for i in nums:
            sum_ = sum_ + i
            if sum_ > 0 and sum_ > max_:
                max_ = sum_
            elif sum_ < 0:
                sum_ = 0
        return max_
