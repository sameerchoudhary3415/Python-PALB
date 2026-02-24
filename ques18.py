class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        
        start = 0
        curr_sum = 0
        min_len = n + 1
        
        for end in range(n):
            curr_sum += arr[end]
            
            while curr_sum > x:
                min_len = min(min_len, end - start + 1)
                curr_sum -= arr[start]
                start += 1
        
        if min_len == n + 1:
            return 0
        
        return min_len
