class Solution:
    def rowWithMax1s(self, arr):
        # code here
        
        n = len(arr)
        m = len(arr[0])

        i = 0
        j = m - 1
        ans = -1

        while i < n and j >= 0:

            if arr[i][j] == 1:
                ans = i
                j -= 1     # move left
            else:
                i += 1     # move down

        return ans
