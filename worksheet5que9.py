class Solution:
    def countLessEqual(self, arr, x):
        #code here
        n = len(arr)
        count = 0

        for i in range(n):
            if arr[i] <= x:
                count += 1

        return count
        
