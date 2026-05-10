class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        if rowIndex == 0:
            return [1]
        prev_arr = []
        for i in range(rowIndex+1):
            curr_arr = []
            for n in range(i+1):
                if n == 0 or n == i:
                    curr_arr.append(1)
                else:
                    num = prev_arr[n] + prev_arr[n-1]
                    curr_arr.append(num)
            prev_arr = curr_arr
            ans.append(curr_arr)
        return ans[-1]
