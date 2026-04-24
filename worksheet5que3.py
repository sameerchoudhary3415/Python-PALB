class Solution:
	def prevSmaller(self, arr):
		# code here# User function Template for python3
        stack = []
        ans = []

        for x in arr:
            # Remove greater or equal elements
            while stack and stack[-1] >= x:
                stack.pop()

            # If stack empty, no previous smaller
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])

            # Push current element
            stack.append(x)

        return ans
