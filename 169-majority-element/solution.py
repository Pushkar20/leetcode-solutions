class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = None
        for n in nums:
            if n != ans:
                if count == 0:
                    ans = n
                else:
                    count -= 1
            else:
                count += 1
        verify = nums.count(ans)
        if verify >= len(nums)/2:
            return ans
