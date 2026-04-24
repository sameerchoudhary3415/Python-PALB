class Solution:
    def countSubarrays(self, arr):
        # code here
        # User function Template for python3

        n = len(arr)
        stack = []
        ans = 0

        # Find next smaller element for each index
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                ans += (i - idx)
            stack.append(i)

        # Remaining elements
        while stack:
            idx = stack.pop()
            ans += (n - idx)

        return ans
