class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows == 0:
            return ans
        prev_arr = []
        for i in range(numRows):
            curr_arr = []
            for n in range(i+1):
                if n == 0 or n == i:
                    curr_arr.append(1)
                else:
                    num = prev_arr[n] + prev_arr[n-1]
                    curr_arr.append(num)
            prev_arr = curr_arr
            ans.append(curr_arr)
        return ans
