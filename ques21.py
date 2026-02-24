class Solution:
    def findMedian(self, arr):
        #code here.
      
        arr.sort()
        n = len(arr)

        # Odd number of elements
        if n % 2 == 1:
            return arr[n // 2]

        # Even number of elements
        else:
            return (arr[n//2 - 1] + arr[n//2]) / 2
