class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 3:
            return sum(nums)
        nums.sort()
        closest = float('inf')

        for i in range(n-2):
            l, r = i+1, n-1

            while l < r:
                t_sum = nums[i] + nums[l] + nums[r]
                if abs(t_sum - target) < abs(closest - target):
                    closest = t_sum
                if t_sum < target:
                    l += 1
                elif t_sum > target:
                    r -= 1
                else:
                    return closest

        return closest
