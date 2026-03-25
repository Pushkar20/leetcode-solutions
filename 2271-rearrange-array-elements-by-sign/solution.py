class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_nums = []
        neg_nums = []
        ans = []
        for i in nums:
            if i > 0:
                pos_nums.append(i)
            else:
                neg_nums.append(i)

        for j in range(len(pos_nums)):
            ans.append(pos_nums[j])
            ans.append(neg_nums[j])
        
        return ans
